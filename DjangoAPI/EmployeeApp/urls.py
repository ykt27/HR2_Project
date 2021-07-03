
from django.conf.urls import url
from EmployeeApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

app_name  = "EmployeeApp"
urlpatterns = [

    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),
    path('departmentDetail/<int:pk>/',views.department_detail), 
    path('viewDepartmentEmployeeList/<int:pk>/',views.department_employee_list),

    #url(r'^employee$',views.employeeApi),
    #url(r'^employee/([0-9]+)$',views.employeeApi),
    #url(r'^SaveFile$', views.SaveFile),
    #url(r'^search$', views.search_all,name='search'),
    #url(r'^attendance$', views.AttendaceApi,name='attendance'),

    path('search', views.employeeSearch),

    path('api/employees/', views.employee_list),
    path('detail/<int:pk>/',views.employee_detail),
    path('create/',views.employee_create),
    path('update/<int:pk>/',views.employee_update),
    path('api/employees/delete/<int:pk>/',views.employee_delete),

    path('attendaceCreate/',views.attendace_create),
    path('attendance/',views.attendance_list),
    path('attendanceHistory/<int:pk>/',views.attendance_history),
    path('attendanceDelete/<int:pk>/',views.attendance_delete),
    path('attendanceUpdate/<int:pk>/',views.attendance_update),

    
    path("upload",views.save_files,name="uploads"),
    path('fileUploadUpdate/<int:pk>/',views.employee_files_update),

    path("createrecordes",views.employee_recordes_create,name="recordescreate"),
    path("getrcordes/<int:pk>/",views.employee_recordes_list),
    path("recordeDelete/<int:pk>/",views.recorde_delete),
    path("recordeUpdate/<int:pk>/",views.recorde_update),
    
    path("createUser",views.create_user),
    path("loginUser",views.login_user),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    
    #urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    