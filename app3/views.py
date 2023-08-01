from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app3_template1(request):
    return render(request,'app3_template1.html')

def app3_template2(request):
    return render(request,'app3_template2.html')

def app3_string(request):
    return HttpResponse('app3_string')