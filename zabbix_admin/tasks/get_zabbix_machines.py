from config import zabbix_user, zabbix_pwd

from zabbix_api import ZabbixAPI

if __name__ == '__main__':
    zapi = ZabbixAPI(server='http://zabbix-server01.dc.nova/zabbix')
    zapi.login(zabbix_user, zabbix_pwd)

    host_response = zapi.host.get({'groupids': [8,9],
                                   'selectInterfaces': 'extend'})
    for host in host_response:
        print(host['host'],host['interfaces'][0]['ip'],  host['hostid'])
