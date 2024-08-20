from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


class Account(View):
    context = ''

    def get(self, request, *args, **kwargs):
        if (self.context == 'login'):
            if (request.user.is_authenticated):
                if (request.user.role == 'cashier'):
                    return redirect('cashier')
                else:
                    return redirect('dashboard')

            return render(request, 'login.html')
                    
        if (self.context == 'logout'):
            logout(request)
            return render(request, 'dashboard.html')

    def post(self, request, *args, **kwargs):
        if (self.context == 'login'):
            user = authenticate(request, request.POST.get('username'), request.POST.get('password'))
            if (user != None):
                login(request, user)
                if (user.role == 'employee'):
                    return redirect('cashier')
                else:
                    return redirect('dashboard')
                
        if (self.context == 'register'):
            logout(request)
            return render(request, 'dashboard.html')

