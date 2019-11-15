from django.db import models

# Create your models here.
#   存放表结构的
class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    state=models.BooleanField
    price=models.DecimalField(max_digits=8,decimal_places=2)  # 123456.78
    pub_date=models.DateTimeField()  # "2018-12-21"
    publish=models.CharField(max_length=32)

    def __str__(self):
        return self.title
