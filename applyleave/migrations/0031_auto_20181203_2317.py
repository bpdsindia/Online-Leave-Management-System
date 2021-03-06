# Generated by Django 2.1 on 2018-12-03 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0030_auto_20181130_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='FY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_year', models.CharField(max_length=10)),
                ('set_current', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 3, 23, 17, 41, 59575), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 3, 23, 17, 41, 62075), null=True),
        ),
    ]
