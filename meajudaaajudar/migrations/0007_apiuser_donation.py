# Generated by Django 3.1.5 on 2021-01-20 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meajudaaajudar', '0006_instituicao'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=500)),
                ('role', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'api_user',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_created=True)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meajudaaajudar.instituicao')),
            ],
            options={
                'db_table': 'donation',
            },
        ),
    ]