# _*_ encoding:utf-8 _*_

import xadmin
from .models import Route,RouteType,RouteIntro,RoutePlan,TravelTeam,FeeDescription,Announcement


class RouteTypeAdmin(object):
    list_display = ['route_type']


class RouteAdmin(object):
    list_display = ['time', 'start_date', 'end_date', 'min_price', 'max_price', 'route', 'power', 'click', 'title']
    search_fields = ['title', 'time', 'start_date', 'end_date', 'max_price', 'min_price', 'click']
    list_filter = ['click', 'title']


class TravelTeamAdmin(object):
    list_display = ['start_date', 'end_date', 'route', 'team', 'status']
    search_fields = ['start_date', 'end_date', 'route', 'team', 'status']
    list_filter = ['start_date', 'end_date', 'status']


class RouteIntroAdmin(object):
    list_display = ['id', 'text']


class RoutePlanAdmin(object):
    list_display = ['id', 'text']


class AnnouncementAdmin(object):
    list_display = ['id', 'text']


class FeeDescriptionAdmin(object):
    list_display = ['id', 'text']


xadmin.site.register(RouteType, RouteTypeAdmin)
xadmin.site.register(Route, RouteAdmin)
xadmin.site.register(TravelTeam, TravelTeamAdmin)
xadmin.site.register(RoutePlan, RoutePlanAdmin)
xadmin.site.register(RouteIntro, RouteIntroAdmin)
xadmin.site.register(Announcement, AnnouncementAdmin)
xadmin.site.register(FeeDescription, FeeDescriptionAdmin)