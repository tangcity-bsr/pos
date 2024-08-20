from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect
from services.utils import role_required

@method_decorator(role_required(['admin', 'root', 'supervisor']), name='dispatch')
class Dashboard(View):
    context = ''

    def get(self, request, *args, **kwargs):
        if (self.context == 'login'):
            return render(request, 'login.html')
        if (self.context == 'dashboard'):
            return render(request, 'dashboard.html')

