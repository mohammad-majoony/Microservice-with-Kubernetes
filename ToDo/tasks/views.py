from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status
from .models import Task


@api_view(['GET'])
def get_all_tasks(request):

    user = request.user

    tasks = Task.objects.all().filter(author=user).order_by('created_date')
    serializers = TaskSerializer(tasks, many=True)

    return Response(serializers.data)


@api_view(['GET'])
def get_task(request, pk):
    try:
        user = request.user
        task = task.objects.get(pk=pk)

        if task.owner != user:
            raise Exception

        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'No task found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def remove_task(request, pk):
    try:
        user = request.user
        task = task.objects.get(pk=pk)

        if task.owner != user:
            raise Exception

        task.delete()

        message = {'detail': 'Task deleted'}
        return Response(message, status=status.HTTP_204_NO_CONTENT)
    except:
        message = {'detail': 'No task found with this id'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_task(request):
    owner = request.data.get('owner')
    title = request.data.get('title')
    description = request.data.get('description')

    task = Task.objects.create(
        owner = owner,
        title = title,
        description = description,
    )

    task.save()
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)