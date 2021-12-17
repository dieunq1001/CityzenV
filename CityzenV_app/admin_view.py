from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from CityzenV_app.models import CustomUser


def admin_home(request):
    return render(request, 'admin_template/admin_base_template.html')


def add_a1(request):
    return render(request, 'admin_template/add_a1_template.html')


def add_a1_save(request):
    if request.method != "POST":
        return HttpResponse("Phương thức không hợp lệ")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=2, is_staff=True, is_superuser=True)
            home_town = "Toàn chi cục"
            user.a1.home_town = home_town
            user.save()
            messages.success(request, "Thêm A1 thành công")
            return HttpResponseRedirect("/add_a1")
        except:
            messages.error(request, "Thêm A1 thất bại")
            return HttpResponseRedirect("/add_a1")


