from django import forms
from django.forms import *

class LoginForm(Form):
    username = CharField(max_length=55, required=True)
    password = CharField(max_length=55, required=True, widget=PasswordInput)
    
class RegisterForm(Form):
    username = CharField(max_length=55, required=True, label=u'Username:')
    email_address = EmailField(required=True, label=u'E-mail Address:')
    password = CharField(max_length=55, required=True, widget=PasswordInput, label=u'Password:')
    password_confirmation = CharField(max_length=55, required=True, widget=PasswordInput, label=u'Again:')