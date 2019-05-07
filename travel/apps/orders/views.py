import logging
import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from django.db.models import Q

from .tasks import *
from .forms import TeamOrderForm, AddUserManForm, AddOrderForm
from users.models import UserMan
from route.models import *
from .models import *


def celery(request):
    """
    add by wth: celery功能测试
    :param request:
    :return:
    """
    celery_test.delay()

    return HttpResponse('celery')

def log_test(request):
    """
    add by wth: logging功能测试
    :param request:
    :return:
    """
    logger = logging.getLogger('django')

    logger.info('this is logging test')
    return HttpResponse('logging')


class TeamOrderView(View):
    """
    团队定制
    """
    def get(self, request):
        date = datetime.date.today()
        return render(request, 'Customized.html', {'date':str(date)})

    def post(self, request):
        teamorder_form = TeamOrderForm(request.POST)
        if teamorder_form.is_valid():
            teamorder = teamorder_form.save(commit=True)
            date = datetime.date.today()
            return render(request, 'Customized.html', {'msg': '信息提交成功','date':str(date)})
        else:
            return render(request, 'Customized.html', {'msg': '信息错误'})


class AddOrderView(View):
    def get(self, request):
        context={}
        theme_id = request.GET.get('theme')
        tour_id = request.GET.get('tour')
        user_id = request.user.id
        user_man = UserMan.objects.filter(Q(user_id=int(user_id))&Q(status='1'))
        tour = Tours.objects.get(Q(theme_id=int(theme_id))&Q(team_num=int(tour_id)))
        theme = TravelTheme.objects.get(id=int(theme_id))
        context['user_man'] = user_man
        context['theme'] = theme
        context['tour'] = tour
        context['user_id'] = user_id
        return render(request, 'Orders_signup.html', context)

    def post(self, request):
        if request.is_ajax():
            add_userman = AddUserManForm(request.POST)
            if add_userman.is_valid():
                context = {}
                user_id = request.user.id
                user_man = add_userman.save(commit=False)
                user_man.user_id = user_id
                user_man.save()
                gender = user_man.gender
                card_type = user_man.card_type
                if gender == '1':
                    gender = '男'
                else:
                    gender = '女'
                if card_type == '0':
                    card_type = '身份证'
                else:
                    card_type = '护照'
                context["name"] = user_man.name
                context["gender"] = gender
                context["card_type"] = card_type
                context["card"] = user_man.card
                context["mobile"] = user_man.mobile
                context["email"] = user_man.email
                context["id"] = user_man.id
                return JsonResponse({"status": "success", "info": context})
            else:
                return JsonResponse({"status": "fail"})
        else:
            add_order = AddOrderForm(request.POST)
            if add_order.is_valid():
                context = {}
                travel_buddy = request.POST.getlist('userman_id')
                img = request.POST.get('img')
                title = request.POST.get('title')
                go_off = request.POST.get('go_off')
                end_time = request.POST.get('end_time')
                order = add_order.save(commit=False)
                tour_id = order.order_tours
                tour = Tours.objects.get(id=tour_id)
                price = tour.price
                order_tours = tour.team_num
                number = len(travel_buddy)
                total = price * number
                status = '0'
                add_time = datetime.now()
                order.order_tours = order_tours
                order.travel_buddy = travel_buddy
                order.number = number
                order.total = total
                order.add_time = add_time
                order.status = status
                order.save()
                id_list = [int(id) for id in travel_buddy]
                man_list = UserMan.objects.filter(id__in=id_list)
                context['img'] = img
                context['title'] = title
                context['go_off'] = go_off
                context['end_time'] = end_time
                context['price'] = price
                context['man_list'] = man_list
                return render(request, 'Order_pay.html', context)


class OrderPayView(View):
    def get(self, request):
        return render(request, 'Order_pay.html', {})


class OrderNewView(View):
    def get(self, request):
        context = {}
        user_id = request.user.id
        orders = OrderDetail.objects.filter(Q(order_user_id=user_id)&Q(status=0))
        man_list = [man.travel_buddy for man in orders]
        theme_id = [int(order.theme) for order in orders]
        tour_id = [int(tour.order_tours) for tour in orders]
        theme = TravelTheme.objects.filter(id__in=theme_id)
        tours = []
        for i in range(len(theme)):
            tour = Tours.objects.get(Q(theme_id=theme[i])&Q(team_num=tour_id[i]))
            tours.append(tour)
        print()
        return render(request, 'Order_now.html', {})


class OrderHisView(View):
    def get(self, request):
        return render(request, 'Order_his.html', {})


class MyInfoView(View):
    def get(self, request):
        return render(request, 'My_info.html', {})


class UpdateInfoView(View):
    def get(self, request):
        return render(request, 'Order_My_C_ModifyInfo.html', {})


class UpdateMobileView(View):
    def get(self, request):
        return render(request, 'Order_My_C_ModifyMobile.html', {})


class UpdateEmailView(View):
    def get(self, request):
        return render(request, 'Order_My_C_ModifyEmail.html', {})


class UpdateManView(View):
    def get(self, request):
        return render(request, 'Order_My_C_ModifyMan.html', {})





