from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_template1(request):
    return render(request,'app1_template1.html')

def app1_template2(request):
    return render(request,'app1_template2.html')

def app1_string(request):
    return HttpResponse('app1_string')