from django.urls import path

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('creden/', views.login_creden, name="user"),
    path('<slug:par>/check', views.choice, name='gtsong'),
    path('addsong/', views.EventList.as_view()),
    path('addsong/<int:pk>/', views.EventDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)