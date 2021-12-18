from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def ShowLoginPage(request):
    return render(request, "login_page.html")


def DoLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method is not allowed</h2>")
    else:
        user = authenticate(request, username=request.POST.get("username"),
                            password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("a1_home"))
            elif user.user_type == "3":
                return HttpResponseRedirect(reverse("a2_home"))
            elif user.user_type == "4":
                return HttpResponseRedirect(reverse("a3_home"))
            elif user.user_type == "5":
                return HttpResponseRedirect(reverse("b1_home"))
            else:
                return HttpResponseRedirect(reverse("b2_home"))
        else:
            messages.error(request, "Tài khoản/mật khẩu không chính xác")
            return HttpResponseRedirect("/")


def DoLogOut(request):
    logout(request)
    return HttpResponseRedirect("/")
