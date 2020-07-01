# from django.shortcuts import render 
# from django.http import HttpResponse
# from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser 
# from rest_framework import status
 
# from .models import Students
# from .serializers import StudentSerializer

# @csrf_exempt
# def students_list(request):
#     if request.method == 'GET':
#         student = Students.objects.all()
#         students_serializer = StudentSerializer(student, many=True)
#         return JsonResponse(students_serializer.data, safe=False)

# @csrf_exempt
# def students_search(request, roll_no):
#     students = Students.objects.filter(roll_no=roll_no)
        
#     if request.method == 'GET': 
#         students_serializer = StudentSerializer(students, many=True)
#         return JsonResponse(students_serializer.data, safe=False)