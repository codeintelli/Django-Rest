from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# * For CRUD Operation You have to create this class


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# * For ReadOnly Operation You have to create this class
# ? Normally, if we are creating API for Covid-19 in which only we can update data at that time this concept is more useful you just have to give api to another and that user can only read data from your api and is you think that you have to give authorization user to perform CRUD on your api then use ModelViewSet.


# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
