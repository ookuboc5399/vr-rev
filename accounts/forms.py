from django import forms
from allauth.account.forms import SignupForm # 追加


class SignupUserForm(SignupForm):
    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.save()
        return user