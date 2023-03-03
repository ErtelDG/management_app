from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('signupInputUserName', 'signupInputEmail', 'signupInputPassword1', 'signupInputPassword2', ) 