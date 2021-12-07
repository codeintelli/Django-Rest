from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

class Student_API(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mes": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

    def put(self, request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mes": "Complete Data Updated"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)


    def patch(self, request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mes": "Partial Data Updated"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

    def delete(self, request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"mes": "Data Deleted"}, status=status.HTTP_200_OK)

        