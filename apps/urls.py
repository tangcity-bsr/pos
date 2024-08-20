from django.contrib import admin
from django.urls import path
from viewer.dashboard import Dashboard
from viewer.gateway import Account

urlpatterns = [
    path('', Dashboard.as_view(context='dashboard')),
    path('login/', Account.as_view(context='login')),
]
