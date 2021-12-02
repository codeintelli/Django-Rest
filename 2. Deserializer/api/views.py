from django.shortcuts import render
from .models import Student
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



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


@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}

            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")