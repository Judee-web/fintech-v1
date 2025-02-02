from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser],  # Ensure admin access

    queryset = User.objects.all()
    serializer_class = UserSerializer




class UserProfileView(APIView):
    def get(self, request):
        # Example response
        data = {
            "user": "John Doe",
            "email": "johndoe@example.com"
        }
        return Response(data, status=status.HTTP_200_OK)