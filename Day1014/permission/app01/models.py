from django.db import models

#   day75  05render的解析

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    # ManyToMany表设计
    roles = models.ManyToManyField("Role")


class Role(models.Model):
    title = models.CharField(max_length=32)
    permissions = models.ManyToManyField("Permission")
    def __str__(self):
        return self.title


class Permission(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=32)
    def __str__(self):
        return self.title
