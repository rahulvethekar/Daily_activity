from bs4 import BeautifulSoup
import requests

def daily_rates_function():
    source = requests.get('http://www.puneapmc.org/rates.aspx?page=rates&catid=1')
    soup = BeautifulSoup(source.content,'html.parser')
    page = soup.find('tr',class_='tr1').find_all('td')
    date_tag = soup.find('td',class_='main_body').find('h1')
    date = date_tag.text.split('-')[1]
    month_name = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    row_date=date.replace(')','').replace('(','').split(',')[1:]
    # print(row_date)
    year=row_date.pop(1)
    # print(row_date)
    row_day_month = row_date
    day = row_day_month[0].split(' ')[1]
    month = row_day_month[0].split(' ')[2]
    # print(day,month)
    date = f'{year}-{month_name.get(month)}-{day}'
    print(date)


    print(page)
    l = []
    daily_record_dict = {}
    for i in page:
        # print(i.text)
        l.append(i.text)

    print(l)
    
    daily_record_dict['Name'] = (l[2])
    daily_record_dict['Measurement'] = l[3]
    daily_record_dict['Total_onion'] = int(l[4])
    daily_record_dict['Minimum_rate'] = int(''.join(filter(lambda i: i.isdigit(), l[5])))
    daily_record_dict['Maximum_rate'] = int(''.join(filter(lambda i: i.isdigit(), l[6])))
    print(daily_record_dict)
    # print(daily_record_dict)

    return daily_record_dict,date

if __name__ =='__main__':

    daily_rates_function()

