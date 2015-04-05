from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'thaipho2/index.html')

def index2(request):
    return render(request, 'thaipho/index.html')