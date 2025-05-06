from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_tasks, name='get_all_tasks'),
    path('add', add_task, name='add_task'),
    path('get/<int:pk>', get_task, name='get_task'),
    path('remove/<int:pk>', remove_task, name='remove_task') 
]
