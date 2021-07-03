from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.contrib.auth import login, authenticate ,logout
from EmployeeApp.models import *
from EmployeeApp.serializers import *
from django.core.files.storage import default_storage
import datetime
from django.contrib.auth.hashers import make_password

# Create your views here.
@api_view(['POST'])
def create_user(request):
    user_data = JSONParser().parse(request)
    user_data['password'] = make_password(user_data['password'])
    print(user_data['password'])
    serializer = User_Serializer(data=user_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        email = user_data.get('email')
        username = user_data.get('username')
        password = user_data.get('password')
        print(make_password(password))
        user = authenticate(request,email=email,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return JsonResponse("Loged in Succeffully!!", safe=False)
    #return Response(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse("Faild Login", safe=False)


@api_view(['POST'])
def employee_recordes_create(request):
    serializer = EmployeeRecordesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def recorde_update(request, pk):
    queryset = Employee_Recordes.objects.get(id=pk)
    serializer = EmployeeRecordesSerializer(instance=queryset, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def employee_recordes_list(request, pk):
    queryset = Employee_Recordes.objects.filter(employees__id=pk)
    serializer = GetEmployeeRecordesSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def department_detail(request, pk):
    queryset = Departments.objects.get(DepartmentId=pk)
    serializer = DepartmentSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def recorde_delete(request, pk):
    queryset = Employee_Recordes.objects.get(id=pk)
    if queryset:
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def department_employee_list(request, pk):
    queryset = Employees.objects.filter(department_id=pk)
    print(queryset[0].department,pk,queryset)
    serializer = EmployeeSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
 
@csrf_exempt
def employeeSearch(request):
    searchItem = JSONParser().parse(request)
    print(searchItem['search'])
    employees_serializer =[]

    if( searchItem['searchType'] == "dep" ):
        department = Departments.objects.filter(DepartmentName=searchItem['search'])
        employees_serializer = DepartmentSerializer(department, many=True)    
    else:
        employees = Employees.objects.filter(EmployeeName=searchItem['search'])
        employees_serializer = EmployeeSerializer(employees, many=True)

    return JsonResponse(employees_serializer.data, safe=False)

#Queryset is a collection of object in the data base
#A Queryset is simply a list of objects from the Django Models. It can be used to query data as Create, Filter, Update, Order etc. 
# Queryset can be written in Django Shell or in views.py.
#if you don't set this argument it means queryset is a single instance and serializer.data will be a single object)

# many=True you tell drf(django-rest-framework) that queryset contains mutiple items (a list of items) so drf needs to serialize each item with serializer 
# class (and serializer.data will be a list)

@api_view(['GET'])
def employee_list(request):
    queryset = Employees.objects.all()
    serializer = EmployeeSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def employee_detail(request, pk):
    queryset = Employees.objects.get(id=pk)
    serializer = EmployeeSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def employee_create(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def employee_update(request, pk):
    queryset = Employees.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=queryset, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def employee_delete(request, pk):
    queryset = Employees.objects.get(id=pk)
    print("queryset", queryset)
    if queryset:
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def attendance_list(request):
    queryset = Attendance.objects.all()
    serializer = AttendanceSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def attendance_update(request, pk):
    queryset = Attendance.objects.get(AttendanceId=pk)
    serializer = AttendanceSerializer(instance=queryset, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def attendance_delete(request, pk):
    queryset = Attendance.objects.get(AttendanceId=pk)
    if queryset:
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def attendace_create(request):
    serializer = SaveAttendanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def attendance_history(request, pk):
    queryset = Attendance.objects.filter(employees=pk)
    print(queryset[0],pk,queryset)
    serializer = AttendanceSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def employee_files_update(request, pk):
    queryset = Employee_Files.objects.get(id=pk)
    serializer = Employee_FilesSerializer(instance=queryset, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def save_files(request):
    serializer = Employee_FilesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)