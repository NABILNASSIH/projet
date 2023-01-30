from django.contrib import admin 
from django.urls import path 
from .views import sayHello 
from . import views
from rest_framework.authtoken.views import obtain_auth_token

  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]
