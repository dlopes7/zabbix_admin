#!/usr/local/sbin/python3.5

import atexit
import json
import ssl

from pyVim import connect
from pyVmomi import vim

from config import vsphere_ip, vsphere_user, vsphere_password


def get_dados_vm(virtual_machine):
    dados = {}
    summary = virtual_machine.summary

    dados['nome'] =  summary.config.name
    dados['os'] = summary.config.guestFullName
    dados['state'] = summary.runtime.powerState

    if summary.guest is not None:
        ip_address = summary.guest.ipAddress
        if ip_address:
            dados['ip'] = ip_address
        else:
            dados['ip'] = None

    if summary.customValue is not None:
        for cv in summary.customValue:
            if cv.key == 501:
                dados['owner'] = cv.value
    return dados


if __name__ == '__main__':

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    context.verify_mode = ssl.CERT_NONE

    service_instance = connect.SmartConnect(host=vsphere_ip,
                                            user=vsphere_user,
                                            pwd=vsphere_password,
                                            port=443,
                                            sslContext=context)


    atexit.register(connect.Disconnect, service_instance)
    content = service_instance.RetrieveContent()

    container = content.rootFolder
    viewType = [vim.VirtualMachine]
    recursive = True

    containerView = content.viewManager.CreateContainerView(
            container, viewType, recursive)

    children = containerView.view
    event_filter = vim.event.EventFilterSpec()
    filter_spec_entity = vim.event.EventFilterSpec.ByEntity()

    full_detalhes = []
    i = 0
    for child in children:
        dados = get_dados_vm(child)
        full_detalhes.append(dados)
        i+=1
        print(i, '/', len(children), dados['nome'])


    with open('servidores.json', 'w') as arq:
        json.dump(full_detalhes, arq)

