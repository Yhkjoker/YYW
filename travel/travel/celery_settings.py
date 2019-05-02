"""
add by wth:

celery配置文件
"""
import djcelery
from celery import platforms
from celery.schedules import crontab


djcelery.setup_loader()

#broker是代理人，它负责分发任务给worker去执行
BROKER_URL = 'redis://127.0.0.1:6379/3'
#导入目标任务文件c
CELERY_IMPORTS = ('orders.tasks','route.tasks','users.tasks')
#设置时区
CELERY_TIMEZONE = 'Asia/Shanghai'
## 定时任务调度器,表示使用了django-celery默认的数据库调度模型,任务执行周期都被存在默认指定的orm数据库中．
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

platforms.C_FORCE_ROOT = True

from datetime import timedelta


CELERYBEAT_SCHEDULE = {
    """
    根据点击量，每三十分钟更新一次主页的热门推荐
    """
    'hot_route': {
        "task": "route.tasks.hot_route",
        "schedule": timedelta(minutes=30),
        "args": (),
    },
}
