from rest_framework import serializers
from .models import Summary

class SummarySerializer(serializers.ModelSerializer):
    """
    Serializer for the Summary model to handle JSON serialization.
    """
    class Meta:
        model = Summary
        fields = '__all__'  # Include all fields
