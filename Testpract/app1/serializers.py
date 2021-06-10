
from .models import Oxygen
from rest_framework import serializers

class Oxyserializer(serializers.ModelSerializer):

    class Meta:
        model=Oxygen
        fields="__all__"