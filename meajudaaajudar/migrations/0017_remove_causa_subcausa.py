# Generated by Django 3.1.5 on 2021-01-25 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meajudaaajudar', '0016_auto_20210123_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='causa',
            name='subCausa',
        ),
    ]