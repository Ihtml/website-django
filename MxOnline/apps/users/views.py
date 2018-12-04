from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import LoginForm


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg":"用户未激活！"})
            else:
                return render(request, "login.html", {"msg":"用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form":login_form})
