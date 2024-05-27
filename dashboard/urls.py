from django.urls import path
from . import views

app_name='dashboard'

urlpatterns =[path('',views.index,name='index'),
              path('logout/',views.logout_user,name='logout'),
              
              
              ]
    

