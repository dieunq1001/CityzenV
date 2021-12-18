from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from CityzenV_app.models import CustomUser, CongDan


def a2_home(request):
    return render(request, 'a2_template/a2_base_template.html')


def add_a3(request):
    return render(request, 'a2_template/add_a3_template.html')


def add_a3_save(request):
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
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=4, is_staff=True)
            user.a3.home_town = home_town
            user.save()
            messages.success(request, "Thêm A3 thành công")
            return HttpResponseRedirect(reverse("a2_add_a3"))
        except:
            messages.error(request, "Thêm A3 thất bại")
            return HttpResponseRedirect(reverse("a2_add_a3"))


def a2_manage_cong_dan(request):
    current_user = request.user
    cong_dans = CongDan.objects.filter(home_town__contains=current_user.a2.home_town)
    return render(request, 'a2_template/a2_manage_cong_dan_template.html', {"cong_dans": cong_dans})
