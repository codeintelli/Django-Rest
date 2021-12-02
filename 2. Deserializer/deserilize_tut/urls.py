
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/<int:pk>',views.student_details),
    path('stu/',views.student_all),
    path('stu/create/',views.student_create),
]
