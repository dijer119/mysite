from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'thaipho/index.html')

def index2(request):
    return render(request, 'thaipho2/index.html')

def about(request):
    return render(request, 'thaipho2/about.html')

def contact(request):
    return render(request, 'thaipho2/contact.html')

def menu(request):
    return render(request, 'thaipho2/menu.html')

