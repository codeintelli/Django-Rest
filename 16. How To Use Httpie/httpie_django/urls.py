
from django.contrib import admin
from django.urls import path, include

from app import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
# for custom auth token in which we can get all details of the user on auth time
from app.auth import CustomAuthtoken 
# creating router object
router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace = 'auth')),
    path('gettoken/', CustomAuthtoken.as_view())
]
