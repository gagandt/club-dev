from django.shortcuts import render
from django.http import HttpResponse

from .models import Event


def index(request):
    latest_events_list = Event.objects.order_by('-organised_on')[:5]
    output = ', '.join([q.description for q in latest_events_list])
    return HttpResponse(output)
    # return HttpResponse(Event.objects.all())

def detail(request, event_id):
    return HttpResponse("You're looking at event %s." % event_id)