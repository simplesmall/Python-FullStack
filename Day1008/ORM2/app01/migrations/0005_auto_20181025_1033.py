# Generated by Django 2.1.1 on 2018-10-25 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_book_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publish',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publish',
        ),
    ]