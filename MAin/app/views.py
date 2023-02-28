from rest_framework.response import Response

from rest_framework.decorators import api_view
from .serializer import *


@api_view(['GET'])
def mainList(request):
    api_list = {
        'List': 'GetBooks/',
        'Create': 'CreateBook/',
        'Update': 'EditBook/<int:pk>',
        'Delete': 'DeleteBook/<int:pk>',
        'Для первого задания нужна приставка': "task_1/"
    }

    return Response(api_list)


@api_view(['GET'])
def bookDetail(request, pk):
    try:
        book = Book.objects.get(id=pk)
        serializer = BookSeriazlier(book, many=False)
        return Response(serializer.data)
    except:
        return Response({'error': 'Нет такой книги'})


@api_view(['POST'])
def bookCreate(request):
    serializer = BookSeriazlier(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def bookList(request):
    books = Book.objects.all().order_by('-id')
    serializer = BookSeriazlier(books, many=True, read_only=True)
    return Response(serializer.data)


@api_view(['POST'])
def bookUpdate(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSeriazlier(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def bookDelete(request, pk):
    try:
        book = Book.objects.get(id=pk)
        name = book.name
        book.delete()
    except:
        return Response({'error': 'Данной книги не существует'})

    return Response(f'Book {name} deleted')
