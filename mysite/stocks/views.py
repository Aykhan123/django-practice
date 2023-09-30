from django.http import HttpResponse
from stocks import stock_helpers


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_latest_data(request):
    print(stock_helpers.get_data())
    return HttpResponse(stock_helpers.get_data())

def get_latest_exchange_rate(request):
    return HttpResponse(stock_helpers.get_exchange_rate('USD', ['JPY', 'EUR']))

def get_all_data(request):
    result = stock_helpers.get_exchange_rate('USD', ['JPY', 'EUR'])
    result += str(stock_helpers.get_data())
    return HttpResponse(result)
