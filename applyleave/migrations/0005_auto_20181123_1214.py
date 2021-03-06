# Generated by Django 2.1 on 2018-11-23 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0004_auto_20181123_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 12, 14, 4, 692490), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='status',
            field=models.SmallIntegerField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('DELETED', 'DELETED'), ('CANCELLED', 'CANCELLED')], null=True),
        ),
    ]
