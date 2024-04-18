from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Goal


# This is where all the views are created.

class UserLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('goals')


class GoalsList(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = 'goals'

class GoalsDetail(LoginRequiredMixin, DetailView):
    model = Goal
    context_object_name = 'goal'
    template_name = 'base/goal.html'

class GoalCreate(LoginRequiredMixin, CreateView):
    model = Goal
    fields = '__all__'
    success_url = reverse_lazy('goals')

class GoalUpdate(LoginRequiredMixin, UpdateView):
    model = Goal
    fields = '__all__'
    success_url = reverse_lazy('goals')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Goal    
    context_object_name = 'goal'
    success_url = reverse_lazy('goals')
