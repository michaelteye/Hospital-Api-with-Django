from django.shortcuts import render
from .models import Drugs
from .serializers import DrugSerializer
from .permission import IsAuthorOrReadOnly
from rest_framework import generics

# Create your views here.
class Personal(generics.ListCreateAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = (IsAuthorOrReadOnly,)
    queryset = Drugs.objects.all()
    serializer_class = DrugSerializer

