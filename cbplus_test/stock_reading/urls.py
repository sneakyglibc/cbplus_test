from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from . import views
from .api import views as api_views

router = DefaultRouter()
router.register(r'stock_readings', api_views.StockReadingViewSet, basename='stock_readings')

urlpatterns = [
    url('api/', include(router.urls)),
    url('stock_reading/', views.stock_reading, name='stock_reading'),
]
