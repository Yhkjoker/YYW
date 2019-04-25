# _*_ encoding:utf-8 _*_

import xadmin

from .models import UserProfile,UserMan
from xadmin import views


class UserProfileAdmin(object):
    list_display = ['username', 'card', 'email', 'mobile', 'date_joined', 'first_name']
    search_fields = ['username', 'card', 'email', 'mobile', 'first_name']
    list_filter = ['date_joined']


class UserManAdmin(object):
    list_display = ['name', 'gender', 'card_type', 'card', 'mobile', 'email', 'status']
    search_fields = ['name', 'gender', 'card_type', 'card', 'mobile', 'email', 'status']
    list_filter = ['gender', 'card_type', 'status']


class GlobalSettings(object):
    site_title = "悠悠蜗后台管理"
    site_footer = "悠悠蜗"
    # menu_style = "accordion"


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(UserMan, UserManAdmin)

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
