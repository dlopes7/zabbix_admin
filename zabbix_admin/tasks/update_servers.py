import json

from zabbix_admin.models import OS, Server

if __name__ == '__main__':
    servers = []
    with open('servidores_zabbix.json', 'r') as servidores_zabbix:
        servers = json.load(servidores_zabbix.read())


    for server in servers:
        new_server = Server(is_host=True,
                            host_name=server['nome'],
                            name=server['nome'],
                            ip=server['ip'],
                            host_id=server['host_id'])
        new_server.save()