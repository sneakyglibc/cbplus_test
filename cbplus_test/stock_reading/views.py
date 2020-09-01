from django.shortcuts import render


def stock_reading(request):
    return render(request, 'stock/stock_reading.html', {})
