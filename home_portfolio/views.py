from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Skills

def home_portfolio(request):
  skills = Skills.objects.all()
  context = {
    'skills':  skills
  }

  return render(request, 'home.html', context)