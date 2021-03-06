# Generated by Django 3.2 on 2021-06-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_recordes',
            name='warning',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='PRESENT', max_length=15),
        ),
        migrations.AlterField(
            model_name='employees',
            name='EmployeeType',
            field=models.CharField(choices=[('full_time', 'FULL_TIME'), ('part_time', 'PART_TIME'), ('contract', 'CONTRACT'), ('intern', 'INTERN')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Recruit',
        ),
    ]
