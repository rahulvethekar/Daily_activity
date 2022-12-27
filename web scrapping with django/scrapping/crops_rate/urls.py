from .views import scrap_onion_details,daily_rates_view
from django.urls import path

urlpatterns = [
    path('get-onion-details/',scrap_onion_details,name='onion_details'),
    path('daily-rates/',daily_rates_view,name='daily_rates'),
]
