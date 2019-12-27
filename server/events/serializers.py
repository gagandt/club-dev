from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """ A serializer for the Event model """
    class Meta:
        model = Event
        fields = ('id', 'name', 'organised_on', 'organising_head', 'organising_budget','description')