# -*- coding: utf-8 -*-
from django import forms
from lifelog.models import Log
import datetime

class LogForm(forms.ModelForm):

    log_date = forms.DateTimeField(initial=datetime.date.today)

    #하위 코드명 이나 간단하게 등록.
    text = forms.CharField(max_length=200, help_text="Please enter the conmmets.")


    class Meta:
        model = Log
        fields = ('log_date', 'text',)
        exclude = ('type',)
