# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class BaseView(View):
    def get(self, request):
        return render(request, "details.html")


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})


class IdenticalListView(View):
    def get(self, request):
        return render(request, 'Identical_list.html', {})


class ShortListView(View):
    def get(self, request):
        return render(request, 'Short_list.html', {})


class LongListView(View):
    def get(self, request):
        return render(request, 'Long_list.html', {})


class CustomizedView(View):
    def get(self, request):
        return render(request, 'Customized.html', {})


class ListDetailsView(View):
    def get(self, request):
        return render(request, 'List_details.html', {})


class OrderSignUpView(View):
    def get(self, request):
        return render(request, 'Orders_signup.html', {})


class CommonProblemView(View):
    def get(self, request):
        return render(request, 'Common_Problem.html', {})


class ContactUsView(View):
    def get(self, request):
        return render(request, 'Contact_Us.html', {})


class DisclaimerView(View):
    def get(self, request):
        return render(request, 'Disclaimer.html', {})


class JoinUs(View):
    def get(self, request):
        return render(request, 'Join_Us.html', {})

