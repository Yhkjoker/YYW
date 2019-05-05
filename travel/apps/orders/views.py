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
                context["name"] = user_man.name
                context["gender"] = user_man.gender
                context["card_type"] = user_man.card_type
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
                bubby = request.POST.get('userman_id')
                return render(request, 'Orders_signup.html', {})






