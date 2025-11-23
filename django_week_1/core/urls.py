from django.urls import path
from . import views

urlpatterns = [
# Quando a URL for a raiz (''), chame a função 'home' de 'views.py'
    path('home/', views.home, name='home'),
    path('segunda/', views.segunda, name='segunda'),
    path('login/', views.login, name='segunda'),
]