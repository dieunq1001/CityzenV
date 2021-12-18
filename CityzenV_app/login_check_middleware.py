from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class login_check_middleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        module_name = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if module_name == "CityzenV_app.admin_view":
                    pass
                elif module_name == "CityzenV_app.views" or module_name == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if module_name == "CityzenV_app.a1_view":
                    pass
                elif module_name == "CityzenV_app.views" or module_name == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("a1_home"))
            elif user.user_type == "3":
                if module_name == "CityzenV_app.a2_view":
                    pass
                elif module_name == "CityzenV_app.views" or module_name == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("a2_home"))
            elif user.user_type == "4":
                if module_name == "CityzenV_app.a3_view":
                    pass
                elif module_name == "CityzenV_app.views" or module_name == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("a3_home"))
            elif user.user_type == "5":
                if module_name == "CityzenV_app.b1_view":
                    pass
                elif module_name == "CityzenV_app.views" or module_name == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("b1_home"))
            elif user.user_type == "6":
                if module_name == "CityzenV_app.b2_view":
                    pass
                elif module_name == "CityzenV_app.views" or module_name == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("b2_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))
        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login"):
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))
