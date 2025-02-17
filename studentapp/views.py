from django.shortcuts import render
from rest_framework .decorators import api_view
from rest_framework .response import Response
from rest_framework import status
from .models import Student
from .serializers import Student_serializer
# Create your views here.
@api_view(['POST'])
def add_student(request):
    serializer = Student_serializer(data = request.data)
    if serializer.is_valid():
         serializer.save()

         return Response(serializer.data, status= status.HTTP_201_CREATED)    
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_students(request):
     students = Student.objects.all()
     serializer = Student_serializer(students,many = True)
     return Response(serializer.data)

@api_view(['GET'])
def view_student(request, pk):
    try:
         student = Student.objects.get(id = pk)

    except Student.DoesNotExist:
         return Response({'error': 'Student not found'}, status= status.HTTP_404_NOT_FOUND)
    serializer = Student_serializer(student)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_student(request , pk):
    try:
         student = Student.objects.get(id = pk)

    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status= status.HTTP_404_NOT_FOUND)
    
    serializer = Student_serializer(student, data = request.data)
    if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
    
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request , pk):
    try:
        student = Student.objects.get(id = pk)

    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status= status.HTTP_404_NOT_FOUND)
    
    student.delete()

    return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

          


             
         