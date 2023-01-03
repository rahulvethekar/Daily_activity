from .views import scrap_onion_details,all_rates_view,get_all_data_from_database,read_csv_view
from django.urls import path

urlpatterns = [
    path('get-onion-details/',scrap_onion_details,name='onion_details'),
    path('get-all-rates/',all_rates_view,name='get_all_rates'),
    path('get-database-data/',get_all_data_from_database,name='get_database_data'),
    path('read-csv/',read_csv_view,name='read_csv'),


]
