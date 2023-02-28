from rest_framework import serializers

from .models import *


class BookSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
