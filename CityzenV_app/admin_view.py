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
        return HttpResponse("<h2>Phuơng thức không hợp lệ</h2>")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        home_town = request.POST.get("home_town")

        try:
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name,
                                                  last_name=last_name, email=email, user_type=2)
            user.a1s.home_town = home_town
            user.save()
            messages.success(request, "Thêm thành công")
            return HttpResponseRedirect("/add_a1")

        except:
            messages.error(request, "Thêm thất bại, vui lòng thử lại sau")
            return HttpResponseRedirect("/add_a1")