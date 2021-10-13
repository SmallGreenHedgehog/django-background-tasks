# Generated by Django 2.2.7 on 2021-10-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background_task', '0003_auto_20210413_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedtask',
            name='repeat',
            field=models.BigIntegerField(choices=[(30, 'every 30 sec'), (60, 'every 1 minute'), (180, 'every 3 minutes'), (300, 'every 5 minutes'), (600, 'every 10 minutes'), (3600, 'hourly'), (86400, 'daily'), (604800, 'weekly'), (1209600, 'every 2 weeks'), (2419200, 'every 4 weeks'), (0, 'never')], default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='repeat',
            field=models.BigIntegerField(choices=[(30, 'every 30 sec'), (60, 'every 1 minute'), (180, 'every 3 minutes'), (300, 'every 5 minutes'), (600, 'every 10 minutes'), (3600, 'hourly'), (86400, 'daily'), (604800, 'weekly'), (1209600, 'every 2 weeks'), (2419200, 'every 4 weeks'), (0, 'never')], default=0),
        ),
    ]
