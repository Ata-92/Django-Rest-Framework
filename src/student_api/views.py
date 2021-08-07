from django.shortcuts import render, HttpResponse
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer

# Create your views here.

def home(request):
    return HttpResponse('<h1>API Page</h1>')

