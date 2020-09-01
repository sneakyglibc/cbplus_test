from django.contrib import admin
from django.urls import include, path

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', include('stock_reading.urls')),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='API Docs', authentication_classes=[], permission_classes=[], public=True)),
]
