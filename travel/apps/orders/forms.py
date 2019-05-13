# _*_ encoding:utf-8 _*_

from django import forms
import re
from captcha.fields import CaptchaField

from .models import TeamOrder, OrderDetail
from users.models import *


class TeamOrderForm(forms.ModelForm):
    class Meta:

        model = TeamOrder
        fields = ['start_place', 'end_place', 'days', 'nature', 'start_time',
                  'end_time', 'budget', 'people_num', 'remarks', 'name', 'phone']

    def clean_phone(self):
        """
        用于匹配手机号是否合法
        """
        mobile = self.cleaned_data['phone']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")


class AddUserManForm(forms.ModelForm):
    class Meta:
        model = UserMan
        exclude = ('user',)

    # def clean_mobile(self):
    #     """
    #     用于匹配手机号是否合法
    #     """
    #     mobile = self.cleaned_data['mobile']
    #     REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
    #     p = re.compile(REGEX_MOBILE)
    #     if p.match(mobile):
    #         return mobile
    #     else:
    #         raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        exclude = ('number', 'total', 'add_date', 'travel_buddy', 'status')


class ModifyInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'card', 'gender']


class UpdateEmailForm(forms.Form):
    email = forms.EmailField(required=True)


class UpdateForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = forms.CharField(required=True)


class ResetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
