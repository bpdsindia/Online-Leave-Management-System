# Generated by Django 2.1 on 2018-11-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20181114_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='employee_setup',
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='employment_setup',
            field=models.CharField(choices=[('Employment', 'Employee'), ('Professional', 'Professional'), ('Intern', 'Intern')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='weekendday',
            name='weekend_day',
            field=models.CharField(max_length=2),
        ),
    ]