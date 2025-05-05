from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_tasks),
    path('add', add_task),
    path('get/<int:task_id>', get_task),
    path('delete/<int:task_id>', remove_task) 
]
