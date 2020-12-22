# Generated by Django 2.2.4 on 2019-09-01 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_book_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=32)),
                ('tel', models.IntegerField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
            ],
        ),
    ]