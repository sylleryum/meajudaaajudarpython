# Generated by Django 3.1.5 on 2021-01-20 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meajudaaajudar', '0005_causa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=2000)),
                ('doar_link', models.CharField(max_length=255)),
                ('imagem', models.CharField(max_length=500)),
                ('nome', models.CharField(max_length=255)),
                ('sobre', models.CharField(max_length=4000)),
                ('url', models.CharField(max_length=255)),
                ('info_doacao', models.CharField(max_length=255)),
                ('causa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meajudaaajudar.causa')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meajudaaajudar.cidade')),
                ('contato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='meajudaaajudar.contato')),
            ],
            options={
                'db_table': 'instituicao',
            },
        ),
    ]