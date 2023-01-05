from django.shortcuts import render
from django.http import HttpResponse
from .scrapper.all_data import all_rates_function
from .models import OnionRate
import pandas as pd
from csv import writer
from logger import logger
# Create your views here.


def all_rates_view(request):
    all_data = all_rates_function.delay()
    # print(all)
    # template_name = 'crops_rate/daily_rate.html'

    # for rate_dict in all_data:
    #     try:
    #         OnionRate.objects.create(crop_name=rate_dict.get('Name'),
    #         measurement=rate_dict.get('Measurement'),
    #         total_onion=rate_dict.get('Total_onion'),
    #         minimum_rate=rate_dict.get('Minimum_rate'),
    #         maximum_rate=rate_dict.get('Maximum_rate'),
    #         date=rate_dict.get('Date'))
    #     except:
    #         logger.error('Duplicates')
    #         continue
    # return render(request,template_name,{'data':daily_rates_dict,'date':date})
    return HttpResponse('Data is scrapping please wait for while!!!!')

def get_all_data_from_database(request):
   data = OnionRate.objects.all()
   wirte_csv_file(data)
   return HttpResponse('Ok')

def read_csv_view(request):
    df = pd.read_csv('data.csv')
    print(df['date'])
    return HttpResponse('done !')


# write csv file function
def wirte_csv_file(data):
    with open('data.csv','w',encoding='utf8',newline='') as f:
        thewriter = writer(f)
        header = ['id','name','measurement','total_onion','minimum_rate','maximun_rate','date']
        thewriter.writerow(header)
        #loading data to csv
        for field in data:
            logger.info('----data loading to csv file------')
            id = field.id
            crop_name = field.crop_name
            measurement = field.measurement
            total_onion = field.total_onion
            minimum_rate = field.minimum_rate
            maximum_rate = field.maximum_rate
            date = field.date
            info = [id,crop_name,measurement,total_onion,minimum_rate,maximum_rate,date]
            thewriter.writerow(info)









