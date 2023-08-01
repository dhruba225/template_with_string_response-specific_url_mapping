app_name='app2'
from django.urls import path
from app2.views import *

urlpatterns=[
    path('app2_template1/',app2_template1,name='app2_template1'),
    path('app2_template2/',app2_template2,name='app2_template2'),
    path('app2_string/',app2_string,name='app2_string'),
]