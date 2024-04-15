from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Goal

# Create your views here.
class GoalsList(ListView):
    model = Goal
    context_object_name = 'goals'

class GoalsDetail(DetailView):
    model = Goal
    context_object_name = 'goal'
    template_name = 'base/goal.html'