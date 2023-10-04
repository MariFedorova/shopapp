from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy

from users.models import User


class LoginView(BaseLoginView):
    #template_name = 'login.html'
    # form = User()
    # return render
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('users:login')


class LogoutView(BaseLogoutView):
    pass
