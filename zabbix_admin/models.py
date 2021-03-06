from django.db import models

class OS(models.Model):
    name = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=(('Linux', 'Linux'), ('Windows', 'Windows')))

    def __str__(self):
        return '{name}'.format(name=self.name,
                                                         tipo=self.tipo)

    class Meta:
        verbose_name_plural = 'OS'

#is_host=True, host_name=, name=, ip=

class Server(models.Model):
    os = models.ForeignKey(OS, null=True)
    is_host = models.BooleanField(default=False)
    host_id = models.IntegerField(null=True, unique=True)
    host_name = models.CharField(max_length=255, null=True)
    is_ignored = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    ip =  models.CharField(max_length=255, unique=True, null=False)
    state = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{name} ({is_host})'.format(name=self.name,
                                                         is_host=self.is_host)

    class Meta:
        verbose_name_plural = 'Servers'


