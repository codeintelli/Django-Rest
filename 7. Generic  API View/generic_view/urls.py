from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # todo: Case 1: Normal API
    # path("student_get/", views.Student_List.as_view()),
    # path("student_get/<int:pk>/", views.Specific_Student.as_view()),
    # path("student_add/", views.Student_Create.as_view()),
    # path("student_edit/<int:pk>/", views.Student_Edit.as_view()),
    # path("student_del/<int:pk>/", views.Student_Delete.as_view()),
    # todo: Case 2: REST API
    path("student_api/", views.Student_LC.as_view()),
    path("student_api/<int:pk>/", views.Student_RUD.as_view()),
] 
