from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} register successfully.")
            return redirect("todo:home")

    else:
        form = RegisterForm()

    context = {"form": form}

    return render(request, "accounts/register.html", context)
