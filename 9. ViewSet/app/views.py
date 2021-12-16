from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        # * for learning about viewset we can perform this
        print('************LIST VIEW**********')
        print('Basename: ', self.basename)
        print('action: ', self.action)
        print('detail: ', self.detail)
        print('suffix: ', self.suffix)
        print('name: ', self.name)
        print('description: ', self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # * for learning about viewset we can perform this
        print('************retrieve VIEW**********')
        print('Basename: ', self.basename)
        print('action: ', self.action)
        print('detail: ', self.detail)
        print('suffix: ', self.suffix)
        print('name: ', self.name)
        print('description: ', self.description)

        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        # * for learning about viewset we can perform this
        print('************create VIEW**********')
        print('Basename: ', self.basename)
        print('action: ', self.action)
        print('detail: ', self.detail)
        print('suffix: ', self.suffix)
        print('name: ', self.name)
        print('description: ', self.description)

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Inserted Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        # * for learning about viewset we can perform this
        print('************update VIEW**********')
        print('Basename: ', self.basename)
        print('action: ', self.action)
        print('detail: ', self.detail)
        print('suffix: ', self.suffix)
        print('name: ', self.name)
        print('description: ', self.description)

        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        # * for learning about viewset we can perform this
        print('************partial_update VIEW**********')
        print('Basename: ', self.basename)
        print('action: ', self.action)
        print('detail: ', self.detail)
        print('suffix: ', self.suffix)
        print('name: ', self.name)
        print('description: ', self.description)

        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # * for learning about viewset we can perform this
        print('************destroy VIEW**********')
        print('Basename: ', self.basename)
        print('action: ', self.action)
        print('detail: ', self.detail)
        print('suffix: ', self.suffix)
        print('name: ', self.name)
        print('description: ', self.description)

        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
