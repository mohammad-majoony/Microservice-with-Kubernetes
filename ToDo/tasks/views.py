from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status
from .models import Task


@api_view(['GET'])
def get_all_tasks(request):

    user = request.user

    tasks = Task.objects.all().filter(owner=user).order_by('created_date')
    serializers = TaskSerializer(tasks, many=True)

    return render(request, 'task_list.html', {'tasks': serializers.data})


@api_view(['GET'])
def get_task(request, pk):
    try:
        user = request.user
        task = Task.objects.get(pk=pk)

        if task.owner != user:
            raise Exception

        serializer = TaskSerializer(task, many=False)
        return render(request, 'task_detail.html', {'task': serializer.data})
    except:
        message = {'detail': 'No task found with this id'}
        return render(request, '404.html', message)


def remove_task(request, pk):
    try:
        user = request.user
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, many=False)

        if task.owner != user:
            raise Exception

        if request.method == 'POST':
            task.delete()
            return redirect(get_all_tasks)

        return render(request, 'remove_task.html', {'task': serializer.data})

    except:
        message = {'detail': 'No task found with this id'}
        return render(request, '404.html', message)


def add_task(request):
    if request.method == 'POST':
        try:
            owner = request.user
            title = request.POST.get('title')
            description = request.POST.get('description')

            task = Task.objects.create(
                owner = owner,
                title = title,
                description = description,
            )

            task.save()
            return redirect(get_all_tasks)

        except:
            message = {'detail': 'Can not add task this time'}
            return render(request, '404.html', message)

    return render(request, 'add_task.html')