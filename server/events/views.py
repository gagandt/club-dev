from django.shortcuts import render
import random
from rest_framework import serializers
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer


def index(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)

def choice(request, par):
    i_events = Event.objects.filter(Q(Genre = par)).distinct()
    random_events = random.sample(list(i_events), 3)
    serializer = EventSerializer(random_events, many=True)
    return JsonResponse(serializer.data, safe=False)

def login_creden(request):
    current_user = request.user
    my_user = str(current_user.username)
    json = {
        'name': my_user
    }
    return JsonResponse(json)

class EventList(generics.ListCreateAPIView):

    queryset = Event.objects.all()

    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Event.objects.all()

    serializer_class = EventSerializer
