from django import forms
from django.contrib.auth import (
    authenticate
)
from django.contrib.auth import get_user_model
User = get_user_model()

class UserLoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget=forms.PasswordInput)
   def clean(self, *args, **kwargs):
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')
      if username and password:
         user = User.objects.filter(username=username)
         if not user:
            raise forms.ValidationError('This superadmin does not exist')
         else:
            user = authenticate(username=username, password=password)
            if not user:
               raise forms.ValidationError('Incorrect password')
      return super(UserLoginForm, self).clean(*args, **kwargs)
