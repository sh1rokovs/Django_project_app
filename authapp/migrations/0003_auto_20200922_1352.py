# Generated by Django 3.1.1 on 2020-09-22 13:52

import authapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20200902_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopuser',
            options={'ordering': ['-is_active', '-is_superuser', '-is_staff', 'username']},
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=authapp.models.get_activation_key_expires),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]