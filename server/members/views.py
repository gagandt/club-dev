from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response

# from .models import Event
from .serializers import UserSerializer

from django.contrib.auth.models import User


def index(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
    # return HttpResponse(User.objects.all())

