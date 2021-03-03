from django.urls import path

from . import viewsets

urlpatterns = [
    path('login/', viewsets.user_login),
    path('sign-up/', viewsets.CreateUser.as_view()),
    path('last-activity/', viewsets.LastActivityRetrieveApiView.as_view()),
    path('last-login/', viewsets.LastLoginRetrieveApiView.as_view()),
]
