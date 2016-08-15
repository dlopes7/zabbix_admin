from django.shortcuts import render
from zabbix_admin.models import Server
from zabbix_admin.tables import ServerTable
from zabbix_admin.tasks import instalador
from django_tables2 import RequestConfig
from django.db.models import Q


def get_table():
    return ServerTable(
        Server.objects.filter(Q(is_ignored=False) & ~Q(name__icontains='HLG') & ~Q(name__icontains='QA') & ~Q(
            name__icontains='TEMPLATE') & ~Q(name__icontains=' ') & ~Q(name__icontains='ligar')))

#& Q(os__name__icontains='windows') & Q(is_host=False))



def servers(request):
    table = get_table()
    RequestConfig(request).configure(table)

    return render(request, 'servers.html', {'table': table})


def instalar(request, server_id):
    server = Server.objects.get(id=server_id)
    resultado = instalador.instalar(server.ip, server.os.name)
    return render(request, 'instalar.html', {'server': server, 'resultado': resultado})


def ignorar(request, server_id):
    server = Server.objects.get(id=server_id)
    server.is_ignored = True
    server.save()

    table = get_table()
    RequestConfig(request).configure(table)

    return render(request, 'servers.html', {'table': table})

