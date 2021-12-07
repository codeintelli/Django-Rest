from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("student_api/", views.Student_API.as_view()),
    path("student_api/<int:pk>", views.Student_API.as_view()),
]
