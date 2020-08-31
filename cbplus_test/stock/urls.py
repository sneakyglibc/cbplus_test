from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .api import views as api_views

router = DefaultRouter()
router.register(r'stock_readings', api_views.StockReadingViewSet, basename='stock_readings')

urlpatterns = [
    path('api/', include(router.urls)),
]
