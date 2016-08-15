from django.shortcuts import render
from zabbix_admin.models import Server
from zabbix_admin.tables import ServerTable

from zabbix_admin.tasks import instalador

from django_tables2 import RequestConfig

def servers(request):
    table = ServerTable(Server.objects.filter(is_ignored=False))
    RequestConfig(request).configure(table)

    return render(request, 'servers.html', {'table': table})


def instalar(request, server_id):
    server = Server.objects.get(id=server_id)
    resultado = instalador.instalar(server.ip, server.os.name)
    return render(request, 'instalar.html', {'server': server, 'resultado': resultado})
