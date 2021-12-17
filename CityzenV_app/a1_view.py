from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from CityzenV_app.models import CustomUser, CongDan


def a1_home(request):
    return render(request, 'a1_template/a1_base_template.html')


def add_a2(request):
    return render(request, 'a1_template/add_a2_template.html')


def add_a2_save(request):
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
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=3, is_staff=True)
            user.a2.home_town = home_town
            user.save()
            messages.success(request, "Thêm A2 thành công")
            return HttpResponseRedirect("/add_a2")
        except:
            messages.error(request, "Thêm A2 thất bại")
            return HttpResponseRedirect("/add_a2")


def manage_cong_dan(request):
    cong_dans = CongDan.objects.all()
    return render(request, 'a1_template/manage_cong_dan_template.html', {"cong_dans": cong_dans})
