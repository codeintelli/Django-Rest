from django.shortcuts import render
from .models import Student
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
# Model Object - Single Student Data
def student_details(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = studentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializer.data, safe=True)


def student_all(request):
    stu = Student.objects.all()
    serializer = studentSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializer.data, safe=False)