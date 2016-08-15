import django_tables2 as tables
from zabbix_admin.models import Server


class ServerTable(tables.Table):
    instalar = tables.TemplateColumn(template_name='botao_instalar.html',
                                     orderable=False,
                                     verbose_name='Instalar')

    ignorar = tables.TemplateColumn(template_name='botao_ignorar.html',
                                    orderable=False,
                                    verbose_name='Ignorar')

    host_id = tables.TemplateColumn(
        '<a target="_blank" href="http://zabbix-server01.dc.nova/zabbix/items.php?filter_set=1&hostid={{record.host_id}}">{{record.host_id|default_if_none:""}}</a>',
    verbose_name="Zabbix")


    class Meta:
        model = Server

        fields = ('is_host', 'name', 'ip', 'os', 'host_id', 'instalar', 'ignorar')
        attrs = {'class': 'paleblue'}
