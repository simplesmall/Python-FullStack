# Generated by Django 2.1.1 on 2018-10-25 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_author_author2book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author2book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='author2book',
            name='book',
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Author2Book',
        ),
    ]