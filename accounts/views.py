from django.views import View
from accounts.models import CustomUser
from django.shortcuts import render, redirect
from allauth.account import views # 追加
from accounts.forms import SignupUserForm


class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class SignupView(views.SignupView):
    template_name = 'accounts/account.html'
    form_class = SignupUserForm