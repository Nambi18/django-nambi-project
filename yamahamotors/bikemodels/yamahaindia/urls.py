from django.urls import path
from . import views

urlpatterns=[
    path('',views.m,name='m'),
    path('service',views.s,name='s'),
    path('r_series',views.v,name='v'),
    path('contact',views.c,name='c'),
    path('mt_series',views.mt,name='mt'),
    path('FZ_series',views.FZ,name='FZ')
    
    
    
]
