from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Event


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')


class EventSerializer(serializers.ModelSerializer):
    """ A serializer for the Event model """
    class Meta:
        model = Event
        fields = ('id', 'name', 'organised_on', 'organising_head', 'organising_budget','description')