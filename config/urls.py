from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    # Управление пользователями
    path('accounts/', include('allauth.urls')),
    # Локальные приложения
    # path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]
