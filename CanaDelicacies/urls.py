
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from CanaDelicacies import settings

urlpatterns = [
    path('', include('canaapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


