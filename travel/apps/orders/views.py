import logging
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .tasks import *
from .forms import TeamOrderForm


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

