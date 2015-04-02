# -*- coding: utf-8 -*-

from django.shortcuts import render
from lifelog.models import Log
from lifelog.form import LogForm

# Create your views here.
def index(request):
    log_list = Log.objects.all()
    context_dict = {'logs': log_list}
    return render(request, 'lifelog/index.html', context_dict)

def food_log_index(request):
    return render(request, 'lifelog/food_log_index.html')

def intro(request):
    # return HttpResponse("Rango says here is the about page. </br>  <a href='/rango/'>Index</a>")
    return render(request, 'lifelog/intro.html')

def regist_form(request):
    logForm = LogForm()
    return render(request, 'lifelog/regist_form.html', {'log': logForm})

def regist(request):
    if request.method == 'POST':
        log = Log(request)
        if log.is_vaild():
            log.save(commit = True)
        else:
            print log.errors
            return render(request, 'lifelog/regist_form.html', {'log': log})
    return index(request);