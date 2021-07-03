from django.db import models
from dateutil.relativedelta import relativedelta
from django.db.models.base import Model
import datetime
from django.contrib.auth.models import AbstractUser,BaseUserManager, PermissionsMixin ,AbstractBaseUser

#from relativedeltafield import RelativeDeltaField
# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.DepartmentName
   
class Employee_Files(models.Model):
    workexperienceUpload = models.FileField(max_length = 100,null=True)
    CVUpload = models.FileField(max_length = 100,null=True)
    otherUpload = models.FileField(max_length = 100,null=True)
    uploaded_at = models.DateField(max_length=100)
    EmployeeName = models.CharField(max_length=100,null=True,default="nnnnn")
    #Employees = models.ForeignKey(EmployeeName, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.EmployeeName  

class Employees(models.Model):
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    STATUS = (('active','ACTIVE'), ('resign', 'RESIGN'), ('vacation', 'VACATION'), ('sick_leave', 'SICK_LEAVE'), ('fired', 'FIRED'), ('layoff', 'LAYOFF'))
    EMPLOYEETYPE = (('full_time','FULL_TIME'), ('part_time','PART_TIME'), ('contract','CONTRACT'), ('intern','INTERN'))
    SHIFT = (('morning_shift','MORNING_SHIFT'), ('night_shift','NIGHT_SHIFT'), ('afternoon_shift','AFTERNOON_SHIFT'))
    id = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100, null=True)
    DateOfJoining = models.DateField(null=True,blank=True)
    PhotoFileName = models.ImageField(upload_to='employee_images', null=True, blank=True)
    Status = models.CharField(max_length=100, choices=STATUS, default = "ACTIVE", null=True)
    StatusDescription = models.CharField(max_length=500, null=True,blank=True)
    Contact = models.CharField(max_length=100, default = "0912345678", null=True)
    Email = models.EmailField(max_length=100, unique=False, default = "example@gmail.com")
    DateOfBirth = models.DateField(max_length=100, null=True)
    #Age= models.IntegerField()
    Gender = models.CharField(choices=GENDER, max_length=100, null=True)
    EmergencyContactName = models.CharField(max_length=100, null=True)
    EmergencyPhone = models.CharField(max_length=100, null=True)
    Citizenship = models.CharField(max_length=100, null=True)
    Race = models.CharField(max_length=100, null=True)
    Education = models.CharField(max_length=100, null=True)
    Salary = models.CharField(max_length=16,default='00,000.00', null=True)
    EmployeeType = models.CharField(choices = EMPLOYEETYPE, max_length=100, null=True)
    Shift = models.CharField(choices=SHIFT, max_length=100, null=True)
    Work_Location = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=100, null=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
    employee_file = models.ForeignKey(Employee_Files, on_delete=models.CASCADE, null=True)
    
    # Null=True , that means it has two possible values for “no data”: NULL , and the empty string Or values.
    # If a field has blank=True , form validation will allow entry of an empty value

    def __str__(self):
        return self.EmployeeName

   
class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'), ('LATE_COME','LATE_COME'), ('EARLY_LEAVE','EARLY_LEAVE'))
    AttendanceId = models.AutoField(primary_key=True)
    status = models.CharField(choices=STATUS, max_length=15 , default="PRESENT")
    employees = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True)
    date = models.DateField(max_length=100)
    #EmployeeName = models.CharField(max_length=100,null=True)

    ''' def __str__(self):
        return self.employees.EmployeeName 
    '''

class Employee_Recordes(models.Model):
    Warning = (('0', '0'), ('1','1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'))
    warning = models.CharField(choices=Warning, max_length=15 , default="PRESENT")
    employees = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True)
    Disciplinary_Description = models.CharField(max_length=500, null=True,blank=True)
    
    def __str__(self):
        return self.Disciplinary_Description 

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(
            username = username,
            email    = self.normalize_email(email),
        )
        user.is_active  = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username,email=email, password=password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username    = models.CharField(max_length=150, unique=True)
    first_name  = models.CharField(max_length=150,null=True)
    last_name   = models.CharField(max_length=150, null=True)
    department  = models.CharField(max_length=250, null=True)
    joindate    = models.DateField(auto_now_add=True,null=True)
    email       = models.EmailField(null=True,unique=True)
    age         = models.IntegerField(null=True)
    phonenumber = models.CharField(max_length=150, unique=True, null=True) 
    is_active   = models.BooleanField(default=True, null=False)
    is_staff    = models.BooleanField(default=False, null=False)
    is_superuser= models.BooleanField(default=False, null=False)


    # profile_image = models.ImageField(upload_to="uploads", blank=False, null=False, default="/static/images/defaultuserimage.jpg")

    objects = MyUserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        fullname = self.first_name + " " + self.last_name
        return fullname

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email


    """ class Recruit(models.Model):
        GENDER = (('male','MALE'), ('female', 'FEMALE'), ('other', 'OTHER'))
        EMPLOYEETYPE = (('Full_Time','FULL_TIME'), ('Part_Time','PART_TIME'), ('Contract','CONTACT'), ('Intern','INTERN'))
        SHIFT = (('Night_Shift','NIGHT_SHIFT'), ('Morning_Sift','MORING_SHIFT'), ('Contract','CONTACT'), ('Intern','INTERN'))
        RecruitmentId = models.AutoField(primary_key=True)
        CandidateName = models.CharField(max_length=100)
        Department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
        PhotoFileName = models.FileField(max_length=100, null=True)
        Contact = models.CharField(max_length=100, default = "0912345678")
        Email = models.EmailField(max_length=100,unique=False , null=False, default = "example@gmail.com")
        DateOfBirth = models.CharField(max_length=100, default = "19-09-1998")
        Gender = models.CharField(choices=GENDER, max_length=100)
        EmergencyContactName = models.CharField(max_length=100)
        EmergencyPhone = models.CharField(max_length=100)
        Citizenship = models.CharField(max_length=100)
        Rase = models.CharField(max_length=100)
        Education = models.CharField(max_length=100)
        EmployeeType = models.CharField(choices=EMPLOYEETYPE, max_length=100)
        Shift = models.CharField(choices=SHIFT, max_length=100)

        def __str__(self):
                return self.CandidateName """
