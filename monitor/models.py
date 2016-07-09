from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=1024)
    password = models.CharField(max_length=1024)

class Server(models.Model):
    alias = models.CharField(max_length=1024)
    uri = models.CharField(max_length=1024)
    status = models.CharField(max_length=1024)
    type = models.CharField(max_length=1024)
    ram = models.IntegerField()
    disk_size = models.IntegerField()
    processor = models.CharField(default="", max_length=1024)


class Stat(models.Model):
    time = models.DateTimeField()
    network_speed = models.IntegerField()
    cpu_load = models.IntegerField()
    cpu_usage = models.IntegerField()
    free_ram = models.IntegerField()
    server = models.ForeignKey(Server)

class ServerSpec(models.Model):
    ram = models.IntegerField()
    disk_size = models.IntegerField()
    processor = models.CharField(default="", max_length=1024)
    server = models.ForeignKey(Server)
