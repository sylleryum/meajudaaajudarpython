# Generated by Django 3.1.5 on 2021-01-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meajudaaajudar', '0008_auto_20210121_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cidadess', to='meajudaaajudar.estado'),
        ),
    ]
