# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password


from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ResetpwdForm
from utils.send_email import send_register_email


# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'Register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_profile = UserProfile()
            username = request.POST.get('email', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            if UserProfile.objects.filter(email=email):
                return render(request, 'Register.html', {'msg': '邮箱已被注册'})
            user_profile.username = username
            user_profile.email = email
            user_profile.is_active = 0
            user_profile.password = make_password(password)
            user_profile.save()

            send_register_email(email)

            return render(request, 'Land.html')
        else:
            return render(request, "Register.html", {"register_form": register_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        all_code = EmailVerifyRecord.objects.filter(code=active_code)
        if all_code:
            for record in all_code:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = 1
                user.save()
                return render(request, 'Land.html')
        else:
            return render(request, 'Register.html')


class ForgetView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "Back.html", {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, send_type='forget')
            return render(request, "response.html", {'email':email})

        else:
            return render(request, "Back.html", {'forget_form': forget_form})


class RetrievePwdView(View):
    def get(self, request, active_code):
        user_code = EmailVerifyRecord.objects.get(code=active_code,send_type='forget')
        email = user_code.email
        return render(request, 'Reset_pwd.html', {'email': email})


class ResetpwdView(View):
    def post(self, request):
        reset_form = ResetpwdForm(request.POST)
        if reset_form.is_valid():
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 != password2:
                return render(request, "Reset_pwd.html", {'msg': '密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(password1)
            user.save()
            return render(request, "Land.html", {})
        else:
            return render(request, "Reset_pwd.html", {'reset_form': reset_form})


class LoginView(View):
    def get(self, request):
        return render(request, "Land.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", '')
            pass_word = request.POST.get("password", '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html", {})
                else:
                    return render(request, 'Land.html', {'msg': '用户未激活'})
            else:
                return render(request, "Land.html", {'msg': '用户名或密码错误'})
        else:
            return render(request, 'Land.html', {'login_form': login_form})
