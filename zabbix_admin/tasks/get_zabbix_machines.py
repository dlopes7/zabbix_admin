from config import zabbix_user, zabbix_pwd

import json

from zabbix_api import ZabbixAPI

if __name__ == '__main__':
    zapi = ZabbixAPI(server='http://zabbix-server01.dc.nova/zabbix')
    zapi.login(zabbix_user, zabbix_pwd)

    host_response = zapi.host.get({'groupids': [8,9],
                                   'selectInterfaces': 'extend'})

    hosts = []
    for host in host_response:
        hosts.append({'nome': host['host'],
                      'ip': host['interfaces'][0]['ip'],
                      'host_id': host['hostid']})


    with open('servidores_zabbix.json', 'w') as arq:
        json.dump(hosts, arq)