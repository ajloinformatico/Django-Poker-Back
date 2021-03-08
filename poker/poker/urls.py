from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from poker import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pokerApp.urls'))  # Include urls from pockerApp
] + static('users/', document_root='./users/')
