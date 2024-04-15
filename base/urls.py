from django.urls import path
from .views import GoalsList, GoalsDetail

urlpatterns = [
    path('', GoalsList.as_view(), name= 'goals'),
    path('goal/<int:pk>/', GoalsDetail.as_view(), name='goal')
]