from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# ? Specially For Browsable API

@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mes": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mes": "Complete Data Updated"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

    if request.method == "PATCH":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mes": "Partial Data Updated"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

    if request.method == "DELETE":
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"mes": "Data Deleted"}, status=status.HTTP_200_OK)