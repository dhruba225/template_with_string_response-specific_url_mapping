app_name='app1'
from django.urls import path
from app1.views import *

urlpatterns=[
    path('app1_template1/',app1_template1,name='app1_template1'),
    path('app1_template2/',app1_template2,name='app1_template2'),
    path('app1_string/',app1_string,name='app1_string'),
]