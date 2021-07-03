from django.http import request
from rest_framework import serializers
from EmployeeApp.models import *
from django.contrib.auth.hashers import make_password

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')

class Employee_FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Files
        fields = '__all__'

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
                  
class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False, read_only=True)
    employee_file = Employee_FilesSerializer(many=False, read_only=True)
    class Meta:
        model = Employees
        #fields = '__all__'
        fields = ('id',
                  'PhotoFileName',
                  'department',
                  'EmployeeName',
                  'department_id',
                  'DateOfJoining',
                  'Status',
                  'Contact',
                  'Email',
                  'DateOfBirth',
                  'Gender',
                  'EmergencyContactName',
                  'EmergencyPhone',
                  'Citizenship',
                  'Race',
                  'Education',
                  'Salary',
                  'EmployeeType',
                  'Shift',
                  'Work_Location',
                  'Address',
                  'employee_file',
                  'employee_file_id',
                  'StatusDescription')

        extra_kwargs = {
                    'department_id': {'source': 'department', 'write_only': True},
                    'employee_file_id': {'source': 'employee_file', 'write_only': True},
                    }


class AttendanceSerializer(serializers.ModelSerializer):
        employees = EmployeeSerializer(many=False, read_only=True)
        class Meta:
            model = Attendance
            fields = ('AttendanceId',
                      'status' ,
                      'employees',
                      'employees_id',
                      'date')    

        extra_kwargs = {
                    'employees_id': {'source': 'employees', 'write_only': True},
                    }

class SaveAttendanceSerializer(serializers.ModelSerializer):
        class Meta:
            model = Attendance
            fields = (  'status' ,
                        'employees',
                        'date')  

class EmployeeRecordesSerializer(serializers.ModelSerializer):
        #employees = EmployeeSerializer(many=False, read_only=True)
        class Meta:
            model = Employee_Recordes
            fields = ('warning' ,
                     'employees',
                     'Disciplinary_Description')    

        """ extra_kwargs = {
                    'employees_id': {'source': 'employees', 'write_only': True},
                    } """

class GetEmployeeRecordesSerializer(serializers.ModelSerializer):
        employees = EmployeeSerializer(many=False, read_only=True)
        class Meta:
            model = Employee_Recordes
            fields = ('id',
                     'warning' ,
                     'employees',
                     'Disciplinary_Description')    









'''class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('RecruitmentId',
                 'CandidateName',
                 'Department',
                 'PhotoFileName',
                 'Contact',
                 'Email'
                 'DateOfBirth',
                 'Gender',
                 'EmergencyContactName',
                 'EmergencyPhone',
                 'Citizenship',
                 'Rase',
                 'EmployeeType',
                 'Education',
                 'Shift',
                 'Address',
                 'Status',
                 'StatusDescription',
                 'Work_Location')
'''




