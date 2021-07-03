# Generated by Django 3.2 on 2021-06-21 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0002_auto_20210621_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('RecruitmentId', models.AutoField(primary_key=True, serialize=False)),
                ('CandidateName', models.CharField(max_length=100)),
                ('PhotoFileName', models.FileField(null=True, upload_to='')),
                ('Contact', models.CharField(default='0912345678', max_length=100)),
                ('Email', models.EmailField(default='example@gmail.com', max_length=100)),
                ('DateOfBirth', models.CharField(default='19-09-1998', max_length=100)),
                ('Gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=100)),
                ('EmergencyContactName', models.CharField(max_length=100)),
                ('EmergencyPhone', models.CharField(max_length=100)),
                ('Citizenship', models.CharField(max_length=100)),
                ('Rase', models.CharField(max_length=100)),
                ('Education', models.CharField(max_length=100)),
                ('EmployeeType', models.CharField(choices=[('Full_Time', 'FULL_TIME'), ('Part_Time', 'PART_TIME'), ('Contract', 'CONTACT'), ('Intern', 'INTERN')], max_length=100)),
                ('Shift', models.CharField(choices=[('Night_Shift', 'NIGHT_SHIFT'), ('Morning_Sift', 'MORING_SHIFT'), ('Contract', 'CONTACT'), ('Intern', 'INTERN')], max_length=100)),
                ('Department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.departments')),
            ],
        ),
    ]