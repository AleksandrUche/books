from django.conf import settings
from django.conf.urls.static import static
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
