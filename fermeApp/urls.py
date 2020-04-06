from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.index, name='index'),
    path('test3', views.test, name='test2'),
] 