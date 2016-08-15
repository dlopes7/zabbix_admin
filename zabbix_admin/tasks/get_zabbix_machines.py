try:
    from config import zabbix_user, zabbix_pwd
except:
    from zabbix_admin.tasks.config import zabbix_user, zabbix_pwd
import json
import os

from zabbix_api import ZabbixAPI

def main():
    zapi = ZabbixAPI(server='http://zabbix-server01.dc.nova/zabbix')
    zapi.login(zabbix_user, zabbix_pwd)

    host_response = zapi.host.get({'groupids': [8,9],
                                   'selectInterfaces': 'extend'})

    hosts = []
    for host in host_response:
        hosts.append({'nome': host['host'],
                      'ip': host['interfaces'][0]['ip'],
                      'host_id': int(host['hostid'])})


    arquivo = os.path.dirname(os.path.realpath(__file__)) + '/servidores_zabbix.json'
    with open(arquivo, 'w') as arq:
        json.dump(hosts, arq)


if __name__ == '__main__':
    main()
