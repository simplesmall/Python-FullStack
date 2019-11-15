from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=32)
    pub_date=models.DateTimeField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    # authors=models.ManyToManyRel(to="Publish")

class Authors(models.Model):
    name=models.CharField(max_length=32)

class Publish(models.Model):
    name=models.CharField(max_length=32)
