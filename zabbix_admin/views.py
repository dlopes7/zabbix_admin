from django.shortcuts import render
from zabbix_admin.models import Server
from zabbix_admin.tables import ServerTable

from django_tables2 import RequestConfig

def servers(request):
    table = ServerTable(Server.objects.filter(is_ignored=False))
    RequestConfig(request).configure(table)

    return render(request, 'servers.html', {'table': table})