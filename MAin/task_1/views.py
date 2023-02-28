from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': 'task-list/',
        'Detail': 'task-detail/<int:pk>/',
        'Create': 'task-create/',
        'Update': 'task-update/<int:pk>/',
        'Delete': 'task-delete/<int:pk>/',
    }

    return Response(api_urls)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    except:
        return Response({'error': 'Нет данной задачи'})


@api_view(['POST'])
def taskUpdate(request, pk):
    # try:
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    # except:
    #     return Response({'error': 'Нет данной задачи'})


@api_view(['DELETE'])
def taskDelete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response(f'{Task.title} deleted')
    except:
        return Response({'error': 'Нет данной задачи'})
