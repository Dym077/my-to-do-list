from django.urls import path
from .views import GoalsList, GoalsDetail, GoalCreate

urlpatterns = [
    path('', GoalsList.as_view(), name= 'goals'),
    path('goal/<int:pk>/', GoalsDetail.as_view(), name='goal'),
    path('goal-create/', GoalCreate.as_view(), name= 'goal-create'),
]