app_name='app3'
from django.urls import path
from app3.views import *

urlpatterns=[
    path('app3_template1/',app3_template1,name='app3_template1'),
    path('app3_template2/',app3_template2,name='app3_template2'),
    path('app3_string/',app3_string,name='app3_string'),
]