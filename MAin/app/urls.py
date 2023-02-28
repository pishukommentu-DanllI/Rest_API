from django.urls import path
from .views import *

urlpatterns = [
    path('', mainList, name='mainList'),
    path('GetBooks/', bookList, name='BookList'),
    path('EditBook/<int:pk>/', bookUpdate, name='EditBook'),
    path('CreateBook/', bookCreate, name='CreateBook'),
    path('DetailBook/<int:pk>/', bookDetail, name='DetailBook'),
    path('DeleteBook/<int:pk>/', bookDelete, name='DeleteBook'),
]
