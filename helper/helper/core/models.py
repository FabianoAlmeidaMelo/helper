from django.db import models

# Create your models here.


class Developer(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=255)
