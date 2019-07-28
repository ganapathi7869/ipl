from django import forms
from iplapp.models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget = forms.TextInput(attrs={'class':'input','placeholder':'Enter Username'})
    )

    password = forms.CharField(
        required = True,
        widget = forms.PasswordInput(attrs={'class':'input','placeholder':'Enter password'})
    )

# class SignUpForm(forms.Form):
#     first_name = forms.CharField(
#         required=True,
#         widget = forms.TextInput(attrs={'class':'input','placeholder':'Enter first name'})
#     )
#
#     last_name = forms.CharField(
#         required=True,
#         widget= forms.TextInput(attrs={'class':'input','placeholder':'Enter last name'})
#     )
#
#     username = forms.CharField(
#         required=True,
#         widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Username'})
#     )
#
#     password = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter password'})
#     )

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['first_name','last_name','username','password', 'profilepic']