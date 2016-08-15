import django_tables2 as tables

from zabbix_admin.models import Server

class ServerTable(tables.Table):

    ignorar = tables.TemplateColumn(template_name='ignorar.html',
                                    orderable=False)

    class Meta:
        model = Server

        fields = ('is_host', 'name', 'ip', 'os', 'host_id', 'ignorar')
        attrs = {'class': 'paleblue'}