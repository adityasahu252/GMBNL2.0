from rest_framework import serializers
from .models import Coustmer


class CoustmerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coustmer
        fields=('id','name','phone_number','username','password')