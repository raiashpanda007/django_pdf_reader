from django.shortcuts import render

# Create your views here.
from .models import CustomUser
from .serializers import Signup
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SignupView(APIView):
    def post (self,request):
        serializer = Signup(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

