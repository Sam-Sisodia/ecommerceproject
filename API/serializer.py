from dataclasses import field
from itertools import product
from rest_framework  import serializers

from app .models import  *



class productserilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"