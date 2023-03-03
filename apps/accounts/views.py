from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User

# signUp view
def signUp_view(request):
    if request.method == "POST":
        print(request.POST.get("signupInputUserName")),
        print(request.POST.get("signupInputEmail")),
        print(request.POST.get("signupInputPassword1")),
        print(request.POST.get("signupInputPassword2")),
        signupInputUserName=request.POST.get("signupInputUserName"),
        signupInputEmail=request.POST.get("signupInputEmail"),
        signupInputPassword1=request.POST.get("signupInputPassword1"),
        signupInputPassword2=request.POST.get("signupInputPassword2"),
        if signupInputPassword1 != signupInputPassword2:
            return render(request, "registration/signup.html", {
            "message": "Passwords must match."
            })
        else:
            user = User.objects.create_user(
            username=signupInputUserName,
            password=signupInputPassword1,
            email=signupInputEmail,
        )
        return render(request, "signup.html")

    

def signup(request):
    return render(request, 'registration/signup.html') 