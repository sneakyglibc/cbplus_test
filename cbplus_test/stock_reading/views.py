from django.conf import settings
from django.shortcuts import render


def stock_reading(request):
    return render(request, 'stock/stock_reading.html',
                  {'url': 'http://127.0.0.1:8000' if settings.DEBUG else 'https://cbplustest.herokuapp.com'})
