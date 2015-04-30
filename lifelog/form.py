# -*- coding: utf-8 -*-
from django import forms
from lifelog.models import Log
from lifelog.models import Code
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import DateTimeInput
import datetime

class LogForm(forms.Form):

    log_date = forms.CharField(max_length=20, widget=forms.HiddenInput())
    #
    # #하위 코드명 이나 간단하게 등록.
    text = forms.CharField(max_length=2000, widget=forms.HiddenInput())
    type = forms.ModelChoiceField(queryset=Code.objects.all())


    class Meta:
        model = Log
        fields = ('type',)
        # exclude = ('log_date')


class LogForm2(forms.ModelForm):

    class Meta:
        model = Log
        fields = ('type', 'text',)
        exclude = ['log_date']
        widgets = {
            'type': forms.Select,
            'text': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
            'log_date' : forms.DateInput(format='%Y-%m-%d %H:%M'),
        }