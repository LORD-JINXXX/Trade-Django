from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/',include('item.urls',namespace='item')),
    path('dashboard/',include('dashboard.urls',namespace='dashboard')),
    path('conversation/',include('conversation.urls',namespace='conversation')),
    path('',include('core.urls',namespace='core'))
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
