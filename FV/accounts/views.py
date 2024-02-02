from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def login_user(request):
      if request.method == "POST":
            username =  request.POST["username"]
            password = request.POST["password"]
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                  login(request, user)
                  return redirect("mangalib:index")
            else:
                  messages.info(request, "Identifiant ou mot de passe incorrect")
                  
      form = AuthenticationForm()
      return render(request, "accounts/login.html", {"form": form})


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("<PASSWORD>")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("mangalib:index")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect("mangalib:index")
