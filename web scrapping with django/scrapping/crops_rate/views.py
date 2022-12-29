from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from .scrapper.onion_rate_scarpper import onion_rate_scrapper 
from .scrapper.daily_rates import daily_rates_function
from .models import OnionRate
# Create your views here.

def scrap_onion_details(request):
    data=onion_rate_scrapper()
    print(data)
    return HttpResponse('scrapping done!')

def daily_rates_view(request):
    daily_rates_dict,date = daily_rates_function()
    template_name = 'crops_rate/daily_rate.html'
    OnionRate.objects.create(crop_name=daily_rates_dict.get('Name'),
    measurement=daily_rates_dict.get('Measurement'),
    total_onion=daily_rates_dict.get('Total_onion'),
    minimum_rate=daily_rates_dict.get('Minimum_rate'),
    maximum_rate=daily_rates_dict.get('Maximum_rate'),
    row_date=date,
    )
    
    return render(request,template_name,{'data':daily_rates_dict,'date':date})








