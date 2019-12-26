from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """ A serializer for the Event model """
    class Meta:
        model = Event
        fields = ('Song','Artist','Genre')