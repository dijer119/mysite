# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'lifelog/index.html')

def intro(request):
    # return HttpResponse("Rango says here is the about page. </br>  <a href='/rango/'>Index</a>")
    return render(request, 'lifelog/intro.html')