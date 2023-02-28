from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name='apiOverview'),
    path('task-list/', taskList, name='task-list'),
    path('task-detail/<int:pk>/', taskDetail, name='task-detail'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-update/<int:pk>/', taskUpdate, name='task-update'),
    path('task-delete/<int:pk>/', taskDelete, name='task-delete')

]
