from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_tasks),
    path('add', add_task),
    path('get/<int:pk>', get_task),
    path('delete/<int:pk>', remove_task) 
]
