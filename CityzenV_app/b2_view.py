from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from CityzenV_app.models import CustomUser, CongDan


def b2_home(request):
    return render(request, 'b2_template/b2_base_template.html')


def add_cong_dan(request):
    return render(request, 'b2_template/add_cong_dan_template.html')


def add_cong_dan_save(request):
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
            return HttpResponseRedirect("/add_cong_dan")
        except:
            messages.error(request, "Thêm công dân thất bại")
            return HttpResponseRedirect("/add_cong_dan")
