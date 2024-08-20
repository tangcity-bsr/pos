from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect
from services.utils import role_required

@method_decorator(role_required(['employee', 'root', 'supervisor']), name='dispatch')
class Dashboard(View):
    context = ''

    def get(self, request, *args, **kwargs):
        if (self.context == 'home'):
            return render(request, 'hom_cashier.html')
