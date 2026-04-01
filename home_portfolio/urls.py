from django.urls import path
from . import views

urlpatterns = [
    path('home_portfolio/', views.home_portfolio, name='home_portfolio'),
]
