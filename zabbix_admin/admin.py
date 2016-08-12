from django.contrib import admin

# Register your models here.

from zabbix_admin.models import OS, Server

admin.site.register(Server)
admin.site.register(OS)