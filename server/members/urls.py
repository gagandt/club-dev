from django.urls import path

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:event_id>/', views.detail, name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)