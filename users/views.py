from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_page(request):
    form = UserRegisterationForm()
    if request.method == "POST":
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f'Account registered for {username} , you can now login!')
            return redirect("login_Barns")
    map = {
        "title" : "Register at Barn's",
        "form" : form
    }
    return render(request,"users/Register_users.html",map)

@login_required
def porfile_users(request):
    map={}
    return render(request,"users/profile_users.html",map)

