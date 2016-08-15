import django_tables2 as tables

from zabbix_admin.models import Server

class ServerTable(tables.Table):

    instalar = tables.TemplateColumn(template_name='botao_instalar.html',
                                    orderable=False,
                                     verbose_name='Instalar')

    ignorar = tables.TemplateColumn(template_name='botao_ignorar.html',
                                    orderable=False,
                                     verbose_name='Ignorar')

    class Meta:
        model = Server

        fields = ('is_host', 'name', 'ip', 'os', 'host_id', 'instalar', 'ignorar')
        attrs = {'class': 'paleblue'}