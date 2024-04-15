from django.urls import path
from .views import GoalsList

urlpatterns = [
    path('', GoalsList.as_view(), name= 'goals'),
]