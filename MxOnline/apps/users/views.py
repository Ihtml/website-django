from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.contrib.auth import authenticate, login


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(user_name, pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
