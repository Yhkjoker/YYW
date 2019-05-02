from celery import task
from .models import *
import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
from apps.utils.redis_connect import REDIS

@task
def hot_route():
    ob = TravelTheme.objects.all().order_by('click_num')[0:2]
    hot_route = []
    for i in ob:
        # 此处需将i.area str化,不然存入redis的值不对劲 0.0
        args = {'area':str(i.area),'img':str(i.img),'title':i.title,'describe':i.describe,'concrete_price':i.concrete_price}
        hot_route.append(args)
    REDIS.set('hot_route',hot_route)
    return True
