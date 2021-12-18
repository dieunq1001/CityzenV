from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from CityzenV_app.models import CustomUser, CongDan


def b1_home(request):
    return render(request, 'b1_template/b1_base_template.html')


def add_b2(request):
    return render(request, 'b1_template/add_b2_template.html')


def add_b2_save(request):
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
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=6, is_staff=True)
            user.b2.home_town = home_town
            user.save()
            messages.success(request, "Thêm B2 thành công")
            return HttpResponseRedirect(reverse("b1_add_b2"))
        except:
            messages.error(request, "Thêm B1 thất bại")
            return HttpResponseRedirect(reverse("b1_add_b2"))


def b1_add_cong_dan(request):
    return render(request, 'b1_template/b1_add_cong_dan_template.html')


def b1_add_cong_dan_save(request):
    if request.method != "POST":
        return HttpResponse("Phương thức không hợp lệ")
    else:
        name = request.POST.get("name")
        identity_id = request.POST.get("identity_id")
        birth_date = request.POST.get("birth_date")
        gender = request.POST.get("gender")
        home_town = request.POST.get("home_town")
        permanent_address = request.POST.get("permanent_address")
        temporary_address = request.POST.get("temporary_address")
        religion = request.POST.get("religion")
        educational_level = request.POST.get("educational_level")
        job = request.POST.get("job")
        try:
            cong_dan = CongDan(name=name, identity_id=identity_id, birth_date=birth_date, gender=gender, home_town=home_town,
                               permanent_address=permanent_address, temporary_address=temporary_address, religion=religion,
                               educational_level=educational_level, job=job)
            cong_dan.save()
            messages.success(request, "Thêm công dân thành công")
            return HttpResponseRedirect(reverse("b1_add_cong_dan"))
        except:
            messages.error(request, "Thêm công dân thất bại")
            return HttpResponseRedirect(reverse("b1_add_cong_dan"))


def b1_manage_cong_dan(request):
    current_user = request.user
    cong_dans = CongDan.objects.filter(home_town__contains=current_user.b1.home_town)
    return render(request, 'b1_template/b1_manage_cong_dan_template.html', {"cong_dans": cong_dans})
