# Generated by Django 3.1.5 on 2021-01-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meajudaaajudar', '0018_auto_20210125_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='logradouro',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='numero',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
