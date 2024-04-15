from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Goal

# Create your views here.
class GoalsList(ListView):
    model = Goal
        