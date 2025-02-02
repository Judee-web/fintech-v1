from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Bill
from .serializers import BillSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
