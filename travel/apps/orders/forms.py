# _*_ encoding:utf-8 _*_

from django import forms
import re

from .models import TeamOrder


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

