import djcelery
from celery import platforms
from celery.schedules import crontab


djcelery.setup_loader()

#broker是代理人，它负责分发任务给worker去执行
BROKER_URL = 'redis://127.0.0.1:6379/3'
#导入目标任务文件
CELERY_IMPORTS = ('orders.tasks','route.tasks','users.tasks')
#设置时区
CELERY_TIMEZONE = 'Asia/Shanghai'
## 定时任务调度器,表示使用了django-celery默认的数据库调度模型,任务执行周期都被存在默认指定的orm数据库中．
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

platforms.C_FORCE_ROOT = True



#定时任务，后续开发会进行补充
# CELERYBEAT_SCHEDULE = {
#     'celery_test': {
#         "task": "appname.tasks.celery_test",
#         "schedule": crontab(minute='*', hour=12),
#         "args": (),
#     },
# }
