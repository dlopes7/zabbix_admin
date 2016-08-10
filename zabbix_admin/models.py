from django.db import models

class OS(models.Model):
    name = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=(('Linux', 'Linux'), ('Windows', 'Windows')))


class Server(models.Model):
    os = models.ForeignKey(OS)
    is_host = models.BooleanField(default=False)
    host_id = models.IntegerField(null=True)
    host_name = models.IntegerField(null=True)
    is_ignored = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    ip =  models.CharField(max_length=255, null=True)



