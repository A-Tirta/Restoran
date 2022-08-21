from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Landing page"),
    path('menu/', views.menu, name="menu page"),
    path('login/', views.login, name="login page")
]