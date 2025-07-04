from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    """Serializer for the Listing model."""
    
    created_by = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'price', 'location',
            'created_by', 'created_at', 'updated_at', 'is_active'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']