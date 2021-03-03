from django.urls import path

from . import viewsets

urlpatterns = [
    path('check-count/', viewsets.CountLikesApiView.as_view()),
]
