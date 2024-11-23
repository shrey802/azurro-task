from rest_framework import serializers
from .models import EnterpriseUser, Turf

class EnterpriseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseUser
        fields = ['uuid','username','email','company_name']
        read_only_fields = ['uuid']


class TurfSerializer(serializers.ModelSerializer):
    owner = EnterpriseUserSerializer(read_only=True)  # Nested serialization for the owner

    class Meta:
        model = Turf
        fields = ['id', 'name', 'location', 'owner', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']