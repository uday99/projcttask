from django.shortcuts import render

from .models import  Oxygen
from  .serializers import Oxyserializer
from  rest_framework.generics import ListAPIView

# Create your views here.

class Businessapi(ListAPIView):
    queryset =Oxygen.objects.all()
    serializer_class = Oxyserializer
