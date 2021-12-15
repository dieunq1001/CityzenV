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
            return HttpResponseRedirect("/admin_home")
            '''if user.userType == "1":
                return HttpResponseRedirect(reverse("adminHome"))
            elif user.userType == "2":
                return HttpResponseRedirect(reverse("teacherHome"))
            else:
                return HttpResponseRedirect(reverse("studentHome"))'''
        else:
            messages.error(request, "Tài khoản/mật khẩu không chính xác")
            return HttpResponseRedirect("/")


def DoLogOut(request):
    logout(request)
    return HttpResponseRedirect("/")
