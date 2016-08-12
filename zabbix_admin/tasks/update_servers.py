import os
import sys
import json
import django

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zabbix_django.settings")
django.setup()

print(sys.path)

from zabbix_admin.models import OS, Server


if __name__ == '__main__':
    servers = []
    with open('servidores_zabbix.json', 'r') as servidores_zabbix:
        servers = json.load(servidores_zabbix)


    for server in servers:
        new_server, created  = Server.objects.get_or_create(is_host=True,
                            host_name=server['nome'],
                            name=server['nome'],
                            ip=server['ip'],
                            host_id=server['host_id'])
        
        print(created, server)
        new_server.save()
