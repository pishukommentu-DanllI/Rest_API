from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('task_1/', include('task_1.urls')),
    path('admin/', admin.site.urls),
]
