from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Goal


# This is where all the views are created.
class GoalsList(ListView):
    model = Goal
    context_object_name = 'goals'

class GoalsDetail(DetailView):
    model = Goal
    context_object_name = 'goal'
    template_name = 'base/goal.html'

class GoalCreate(CreateView):
    model = Goal
    fields = '__all__'
    success_url = reverse_lazy('goals')

class GoalUpdate(UpdateView):
    model = Goal
    fields = '__all__'
    success_url = reverse_lazy('goals')

class DeleteView(DeleteView):
    model = Goal    
    context_object_name = 'goal'
    success_url = reverse_lazy('goals')
