from django.contrib import admin
from django.urls import path
from viewer.dashboard import Dashboard

urlpatterns = [
    path('', Dashboard.as_view(context='dashboard')),
]
