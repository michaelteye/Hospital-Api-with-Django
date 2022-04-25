from django.db.models import fields
from rest_framework import serializers
from .models import Drugs


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = ('name', 'disease', 'symptoms','time', 'drug_type', 'prescription')