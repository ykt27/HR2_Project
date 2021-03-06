# Generated by Django 3.2 on 2021-06-06 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workexperienceUpload', models.FileField(null=True, upload_to='')),
                ('CVUpload', models.FileField(null=True, upload_to='')),
                ('otherUpload', models.FileField(null=True, upload_to='')),
                ('uploaded_at', models.DateField(max_length=100)),
                ('EmployeeName', models.CharField(default='nnnnn', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('department', models.CharField(max_length=250, null=True)),
                ('joindate', models.DateField(auto_now_add=True, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('age', models.IntegerField(null=True)),
                ('phonenumber', models.CharField(max_length=150, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
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
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=100, null=True)),
                ('DateOfJoining', models.DateField(blank=True, null=True)),
                ('PhotoFileName', models.ImageField(blank=True, null=True, upload_to='employee_images')),
                ('Status', models.CharField(choices=[('active', 'ACTIVE'), ('resign', 'RESIGN'), ('vacation', 'VACATION'), ('sick_leave', 'SICK_LEAVE'), ('fired', 'FIRED'), ('layoff', 'LAYOFF')], default='ACTIVE', max_length=100, null=True)),
                ('StatusDescription', models.CharField(blank=True, max_length=500, null=True)),
                ('Contact', models.CharField(default='0912345678', max_length=100, null=True)),
                ('Email', models.EmailField(default='example@gmail.com', max_length=100)),
                ('DateOfBirth', models.DateField(max_length=100, null=True)),
                ('Gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=100, null=True)),
                ('EmergencyContactName', models.CharField(max_length=100, null=True)),
                ('EmergencyPhone', models.CharField(max_length=100, null=True)),
                ('Citizenship', models.CharField(max_length=100, null=True)),
                ('Race', models.CharField(max_length=100, null=True)),
                ('Education', models.CharField(max_length=100, null=True)),
                ('Salary', models.CharField(default='00,000.00', max_length=16, null=True)),
                ('EmployeeType', models.CharField(choices=[('full_time', 'FULL_TIME'), ('part_time', 'PART_TIME'), ('contract', 'CONTACT'), ('intern', 'INTERN')], max_length=100, null=True)),
                ('Shift', models.CharField(choices=[('morning_shift', 'MORNING_SHIFT'), ('night_shift', 'NIGHT_SHIFT'), ('afternoon_shift', 'AFTERNOON_SHIFT')], max_length=100, null=True)),
                ('Work_Location', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.departments')),
                ('employee_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.employee_files')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Recordes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warning', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='PRESENT', max_length=15)),
                ('Disciplinary_Description', models.CharField(blank=True, max_length=500, null=True)),
                ('employees', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EmployeeApp.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('AttendanceId', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'), ('LATE_COME', 'LATE_COME'), ('EARLY_LEAVE', 'EARLY_LEAVE')], default='PRESENT', max_length=15)),
                ('date', models.DateField(max_length=100)),
                ('employees', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EmployeeApp.employees')),
            ],
        ),
    ]
