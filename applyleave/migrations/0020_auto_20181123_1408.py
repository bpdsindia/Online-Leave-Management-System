# Generated by Django 2.1 on 2018-11-23 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0019_auto_20181123_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('DELETED', 'DELETED'), ('CANCELLED', 'CANCELLED')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 14, 8, 13, 538132), null=True),
        ),
    ]