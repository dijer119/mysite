# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect

from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from lifelog.models import Log, Code
from lifelog.form import LogForm, LogForm2
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    log_list = Log.objects.order_by('-log_date')
    context_dict = {'logs': log_list}

    return render(request, 'lifelog/index.html', context_dict)

class IndexView(TemplateView):
    template_name = 'lifelog/index2.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lines = []
        log_list = Log.objects.order_by('-log_date')
        paginator = Paginator(log_list, 20)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context

class ModifyFormView(TemplateView):
    template_name = 'lifelog/modify_form.html'

    def get_context_data(self, **kwargs):
        context = super(ModifyFormView, self).get_context_data(**kwargs)
        log_id = self.kwargs['log_id']
        log = Log.objects.get(pk=log_id)
        log_form = LogForm2(instance=log)
        # log_form['log_date'].initial=log.log_date
        context['form'] = log_form
        context['log_date'] = log.log_date
        context['log_id'] = log_id
        return context

class ModifyView(UpdateView):
    template_name = 'lifelog/modify_form.html'

    def get_context_data(self, **kwargs):
        context = super(ModifyFormView, self).get_context_data(**kwargs)
        log_id = self.kwargs['log_id']
        log = Log.objects.get(pk=log_id)
        log_form = LogForm2(self.request.POST, instance=log)
        if log_form.is_valid():
            log_form.save();
        return HttpResponseRedirect('/')

def modify(request, log_id):
    if request.method == 'POST':
        # log_id = request.POST['log_id']
        log = Log.objects.get(pk=log_id)
        log_form = LogForm2(request.POST, instance=log)
        if log_form.is_valid():
            log_form.save();
    # return render(request, 'index')
    return HttpResponsePermanentRedirect("/lifelog/")


def food_list(request):
    return render(request, 'lifelog/food_log_index.html')

def food_log_index(request):
    return render(request, 'lifelog/food_log_index.html')

def intro(request):
    # return HttpResponse("Rango says here is the about page. </br>  <a href='/rango/'>Index</a>")
    return render(request, 'lifelog/intro.html')

def regist_form(request):
    logForm = LogForm()
    code_list = Code.objects.all();
    context_dict = {'logs': logForm,
                    'code_list':code_list}
    return render(request, 'lifelog/regist_form.html', context_dict)

def regist_form2(request):
    logForm = LogForm2()
    context_dict = {'form': logForm}
    return render(request, 'lifelog/regist_form2.html', context_dict)

def modify_form(request):
    logForm = LogForm()
    code_list = Code.objects.all();
    context_dict = {'logs': logForm,
                    'code_list':code_list}
    return render(request, 'lifelog/regist_form.html', context_dict)

def regist(request):

    if request.method == 'POST':
        logForm = LogForm(request.POST)
        if logForm.is_valid() :
            logger.debug(logForm.cleaned_data)
            logger.debug(request.POST['type'])
            logger.debug(logForm.cleaned_data['type'])
            logger.debug(request.POST['log_date'])
            logger.debug(request.POST['text'])
            codes = Code.objects.all()
            for code in codes:
                logger.debug(code.code +':'+code.code_name)
            code = Code.objects.get(code=(request.POST['type']));
            log = Log(log_date=request.POST['log_date'], type=code, text=request.POST['text']);
            log.save();
    return HttpResponsePermanentRedirect("/lifelog/");

def regist2(request):

    if request.method == 'POST':
        logForm = LogForm2(request.POST)
        if logForm.is_valid() :
            new_log = logForm.save(commit=False)
            new_log.log_date = request.POST['log_date']
            new_log.save()
    return HttpResponsePermanentRedirect("/lifelog/");

