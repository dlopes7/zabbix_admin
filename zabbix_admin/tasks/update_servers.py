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
from django.db.models import Q


def populate_from_zabbix():
    arquivo = os.path.dirname(os.path.realpath(__file__)) + '/servidores_zabbix.json'

    with open(arquivo, 'r') as servidores_zabbix:
        servers = json.load(servidores_zabbix)


    for server in servers:
        print(server)
        new_server, created = Server.objects.get_or_create(
                            ip=server['ip'])

        #print('ZABBIX', created, server)
        new_server.is_host = True
        new_server.host_id = server['host_id']
        new_server.host_name = server['nome']
        new_server.name = server['nome']
        new_server.ip = server['ip']

        try:
            new_server.save()
        except Exception as e:

            print('Erro:', e)
            continue

        #print('ZABBIX', server, new_server.is_host)

def populate_from_vsphere():
    arquivo = os.path.dirname(os.path.realpath(__file__)) + '/servidores_vsphere.json'
    with open(arquivo, 'r') as servidores_vsphere:
        servers = json.load(servidores_vsphere)

    for server in servers:
        if server['ip'] is not None:
            new_os, created = OS.objects.get_or_create(name=server['os'])


            try:
                server_zabbix = Server.objects.get(name=server['nome'])
                #print('VSPHERE', 'Setando OS para', server_zabbix, new_os)
                server_zabbix.os = new_os
                server_zabbix.state = server['state']
                server_zabbix.save()

            except:

                try:
                    server_zabbix = Server.objects.get(ip=server['ip'])
                    server_zabbix.os = new_os
                    server_zabbix.state = server['state']
                    server_zabbix.save()



                except Exception as e:
                    print('VSPHERE', server['nome'], 'does not exist on zabbix')
                    try:
                        server_vsphere, created = Server.objects.get_or_create(name=server['nome'],
                                                                      ip=server['ip'],
                                                                      is_host=False,
                                                                      os=new_os,
                                                                      state=server['state']
                                                                      )

                        server_vsphere.save()
                    except Exception as e:
                        print('VSPHERE', 'ERRO:', server, e)



def main():
    populate_from_zabbix()
    populate_from_vsphere()

if __name__ == '__main__':
    main()




