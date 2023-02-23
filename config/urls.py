from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    # Управление пользователями
    path('accounts/', include('allauth.urls')),
    # Локальные приложения
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
]
