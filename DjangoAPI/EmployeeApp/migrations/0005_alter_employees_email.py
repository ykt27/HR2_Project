# Generated by Django 3.2 on 2021-06-30 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0004_delete_recruit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Email',
            field=models.EmailField(default='example@gmail.com', max_length=100, unique=True),
        ),
    ]
