# Generated by Django 2.1 on 2018-11-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0020_auto_20181116_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employmentsetup',
            name='id',
        ),
        migrations.AlterField(
            model_name='employmentsetup',
            name='employment_setup',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
