from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signIn/', views.signIn, name='signIn'),
    path('signup/', views.signup, name='signup'),
]
