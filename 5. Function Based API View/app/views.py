from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your view here

# * By default it will be get method


# @api_view()
# def hello_world(request):
#     return Response({'mes': 'Har Har Mahadev'})

# * if we want to POST method then


# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({'mes': 'GET Request Accepted'})
#     # return Response({'mes': 'GET Request Rejected'})

#     if request.method == 'POST':
#         print(request.data)
#         return Response({'mes': 'Post request accepted'})
#     return Response({'mes': 'post request rejected'})


# todo CRUD API using Functional Based API View
# * this is only for practice and this will only run in myapi.py file for browsable API See Below code
# @api_view(["GET", "POST", "PUT", "DELETE"])
# def student_api(request):
#     if request.method == "GET":
#         id = request.data.get("id")
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"mes": "Data Created"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

#     if request.method == "PUT":
#         id = request.data.get("id")
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"mes": "Data Updated"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

#     if request.method == "DELETE":
#         id = request.data.get("id")
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({"mes": "Data Deleted"}, status=status.HTTP_200_OK)


# ? Specially For Browsable API


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
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
