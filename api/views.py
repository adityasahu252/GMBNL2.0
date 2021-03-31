from django.shortcuts import render
from rest_framework import viewsets
from .models import Coustmer
from .serialzier import CoustmerSerializer
# Create your views here.

class CoustmerViewset(viewsets.ModelViewSet):
    serializer_class=CoustmerSerializer
    queryset=Coustmer.objects.all()