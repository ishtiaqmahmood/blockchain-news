# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    # Grab crypto currency price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX,XMR&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    # Grab crypto news data
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")  
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api' : api, 'price' : price})

