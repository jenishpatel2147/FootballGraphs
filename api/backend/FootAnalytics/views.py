from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FootGraphSerializer
from .models import FootGraph

# Create your views here.

class FootView(viewsets.ModelViewSet):
    serializer_class = FootGraphSerializer
    queryset = FootGraph.objects.all()

# Create your views here.
