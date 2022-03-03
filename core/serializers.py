from rest_framework.serializers import ModelSerializer,SerializerMethodField
from . models import *

class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'seats', 'status']