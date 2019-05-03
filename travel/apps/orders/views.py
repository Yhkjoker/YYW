import logging
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.db.models import Q

from .tasks import *
from .forms import TeamOrderForm, AddUserManForm
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
        user_man = UserMan.objects.filter(user_id=int(user_id))
        tour = Tours.objects.get(Q(theme_id=int(theme_id))&Q(team_num=int(tour_id)))
        theme = TravelTheme.objects.get(id=int(theme_id))
        context['user_man'] = user_man
        context['theme'] = theme
        context['tour'] = tour
        return render(request, 'Orders_signup.html', context)


class AddUserMan(View):
    def post(self,request):
        add_userman = AddUserManForm(request.POST)
        if add_userman.is_valid():
            user_id = request.user.id
            user_man = UserMan()
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            card = request.POST.get('card')
            card_type = request.POST.get('card_type')
            status = request.POST.get('status')
            user_man.name = name
            user_man.gender = gender
            user_man.mobile = mobile
            user_man.email = email
            user_man.card = card
            user_man.card_type = card_type
            user_man.status = status
            user_man.user_id = user_id
            user_man.save()




