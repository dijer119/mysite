# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# class User(models.Model):
#     create_date = models.DateTimeField('Create Date')
#     update_date = models.DateTimeField('Update Date')
#
#     #email 고려
#     user_id = models.CharField(max_length=200)
#
class Code(models.Model):
    code = models.CharField(max_length=10)
    code_name = models.CharField(max_length=50)
    p_code = models.CharField(max_length=10)
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.code_name

class Log(models.Model):
    create_date = models.DateTimeField('Create Date')
    update_date = models.DateTimeField('Update Date')

    #실제 log 발생한 일시
    log_date = models.DateTimeField('Event Date')

    #log type, 약, 운동, 먹는거 등등.
    type = models.ForeignKey(Code)

    #하위 코드명 이나 간단하게 등록.
    text = models.CharField(max_length=200)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.text

#
#     #
#
#
#     user = models.ForeignKey(User)
#
