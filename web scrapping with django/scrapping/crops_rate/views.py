from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from .scrapper.onion_rate_scarpper import onion_rate_scrapper 
from .scrapper.daily_rates import daily_rates_function
# Create your views here.

def scrap_onion_details(request):
    data=onion_rate_scrapper()
    print(data)
    return HttpResponse('scrapping done!')

def daily_rates_view(request):
    daily_rates_dict = daily_rates_function()
    template_name = 'crops_rate/daily_rate.html'
    
    return render(request,template_name,{'data':daily_rates_dict})








