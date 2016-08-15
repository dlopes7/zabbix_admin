from django.conf.urls import url

from zabbix_admin import views

urlpatterns = [
    url(r'^$', views.servers, name='servers'),

]