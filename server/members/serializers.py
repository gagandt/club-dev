from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'is_active', 'is_superuser')