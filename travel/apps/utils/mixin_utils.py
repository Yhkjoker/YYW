from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
"""类的方法和独立的函数不完全相同，所以你不可以直接将函数装饰器运用到方法上
 —— 你首先需要将它转换成一个方法装饰器。
"""

class LoginRequiredMixin(object):
    """
    add by wth:
    视图类继承此混合类即可拥有login_required功能(使用时一定要将此混合类放在mro第一顺位)
    """
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)