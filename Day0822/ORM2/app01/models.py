from django.db import models

# Create your models here.
class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    pub_date=models.DateTimeField()
    publish=models.ForeignKey(to="Publish",on_delete=models.CASCADE,null=True) #级联删除
    #  此处的to里面的参数可以加"",也可以不加,加的时候参数在前面位置或者后面位置都无所谓,但是不加的话参数位置只能在后面
    authors=models.ManyToManyField(to="Author")  # 该句代码生成Author2Book表

    def __str__(self):
        return self.title

class Publish(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
    # def __str__(self):
    #     return self.name

class Author(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    email=models.CharField(max_length=32)
    # 原始的一对一关系表建立语句
    ad=models.ForeignKey("AuthorDetail",on_delete=models.CASCADE,unique=True)
    # 另外一种一对一的写法
    # ad=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    addr=models.CharField(max_length=32)
    tel=models.IntegerField()
    # 一对一的情况下用其中一张表来限定另一张表随便在哪张表里面指定都是一样的
    # author=models.OneToOneField("Author",on_delete=models.CASCADE)
    def __str__(self):
        return self.addr

# class Author2Book(models.Model):
#     nid=models.AutoField(primary_key=True)
#     book=models.ForeignKey(to="Book",on_delete=models.CASCADE)
#     author=models.ForeignKey(to="Author",on_delete=models.CASCADE)

class Emp(models.Model):
    name=models.CharField(max_length=32)
    dep=models.CharField(max_length=32)
    sal=models.DecimalField(max_digits=8,decimal_places=2)
    addr=models.CharField(max_length=32)