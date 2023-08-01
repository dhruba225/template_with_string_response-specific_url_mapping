from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_template1(request):
    return render(request,'app2_template1.html')

def app2_template2(request):
    return render(request,'app2_template2.html')

def app2_string(request):
    return HttpResponse('app2_string')