# Generated by Django 2.2 on 2020-09-07 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200902_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['name']},
        ),
    ]