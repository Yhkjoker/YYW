# _*_ encoding:utf-8 _*_

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from travel.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == 'register':
        code = random_str(8)
    else:
        code = random_str(4)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = '悠悠蜗大学生旅游网激活'
        email_body = '请点击网址进行账号激活http://127.0.0.1:8000/active/{0}'.format(code)

        email_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if email_status:
            pass
    elif send_type == 'forget':
        email_title = '悠悠蜗大学生旅游网密码找回'
        email_body = '请点击网址进行账号激活http://127.0.0.1:8000/retrievepwd/{0}'.format(code)

        email_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if email_status:
            pass
    elif send_type == 'update':
        email_title = '悠悠蜗大学生旅游网邮箱更新'
        email_body = '您的验证码为{}'.format(code)

        email_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if email_status:
            pass

    elif send_type == 'reset':
        email_title = '悠悠蜗大学生旅游网密码重置'
        email_body = '您的验证码为{}'.format(code)

        email_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if email_status:
            pass





