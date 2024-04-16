from django.urls import path
from .views import GoalsList, GoalsDetail, GoalCreate, GoalUpdate, DeleteView, UserLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', GoalsList.as_view(), name='goals'),
    path('goal/<int:pk>/', GoalsDetail.as_view(), name='goal'),
    path('goal-create/', GoalCreate.as_view(), name= 'goal-create'),
    path('goal-update/<int:pk>/', GoalUpdate.as_view(), name='goal-update'),
    path('goal-delete/<int:pk>/', DeleteView.as_view(), name='goal-delete'),
]