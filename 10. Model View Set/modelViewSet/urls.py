from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter

# todo creating router object
router = DefaultRouter()

# todo Register studentViewSet with Router

# * For CRUD Operation You have to create this class
router.register('studentapi', views.StudentModelViewSet, basename='student')

# * For ReadOnly Operation You have to create this class
# router.register('studentapi', views.StudentReadOnlyModelViewSet,
#                 basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
