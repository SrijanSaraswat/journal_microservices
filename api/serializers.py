
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Journal, UserRole

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'description', 'attachment_type', 'published_at']

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['user', 'role']
