import django_tables2 as tables

from zabbix_admin.models import Server

class ServerTable(tables.Table):

    instalar = tables.TemplateColumn(template_name='ignorar.html',
                                    orderable=False,
                                     verbose_name='Instalar')

    class Meta:
        model = Server

        fields = ('is_host', 'name', 'ip', 'os', 'host_id', 'instalar')
        attrs = {'class': 'paleblue'}