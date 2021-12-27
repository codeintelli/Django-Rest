from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # * when we are using global authentication then we don't need to add it all
    # authentication_classes = [BasicAuthentication]
    # * here we can give many classes in single permission 
    # permission_classes = [IsAuthenticated, AllowAny]
    # permission_classes = [IsAuthenticated]
    # * here if only show api to Admin for other user it shows 
    # ! "detail": "You do not have permission to perform this action."
    permission_classes = [IsAdminUser]
