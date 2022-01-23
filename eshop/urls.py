from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('', admin.site.urls),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
