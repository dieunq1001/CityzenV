from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from CityzenV_app.models import CustomUser


def a3_home(request):
    return render(request, 'a3_template/a3_base_template.html')


def add_b1(request):
    return render(request, 'a3_template/add_b1_template.html')


def add_b1_save(request):
    if request.method != "POST":
        return HttpResponse("Phương thức không hợp lệ")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        home_town = request.POST.get("home_town")

        try:
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=5, is_staff=True)
            user.b1.home_town = home_town
            user.save()
            messages.success(request, "Thêm B1 thành công")
            return HttpResponseRedirect("/add_b1")
        except:
            messages.error(request, "Thêm B1 thất bại")
            return HttpResponseRedirect("/add_b1")