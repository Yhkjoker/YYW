from celery import task


@task
def celery_test():
    print('======celery=====')
