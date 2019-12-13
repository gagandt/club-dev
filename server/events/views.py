from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


def index(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)
    # return HttpResponse(Event.objects.all())

def detail(request, event_id):
    return HttpResponse("You're looking at event %s." % event_id)