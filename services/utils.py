from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            _deny_page = render(request, 'base/403.html')
            _deny_page.status_code = 403
            return _deny_page
        return _wrapped_view
    return decorator
