from django.shortcuts import render, redirect
from django.contrib.auth.models import User 


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)

# def index(request):
#     return render(request, 'chat/index.html')