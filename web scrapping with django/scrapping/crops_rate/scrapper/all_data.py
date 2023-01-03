from bs4 import BeautifulSoup
import requests
import time
import datetime
all_record_list = []

def all_rates_function():
    for no in range(3292,3297+1):
        try:
            source = requests.get('http://www.puneapmc.org/history.aspx?id=Rates'+str(no))
            soup = BeautifulSoup(source.content,'html.parser')
            page = soup.find('tr',class_='tr0').find_all('td')
            print(no)
            date_tag = soup.find('form',id='form1').find('h2')
            # print(date_tag)
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
            # date = f'{year}-{month_name.get(month)}-{day}'
            # print(type(year))
            # print(type(month_name.get(month)))
            date = datetime.date(int(year),month_name.get(month),int(day))
            # print(date)

            # date = date_tag.text.split('-')[1]

            # print(page)
            l = []
            daily_record_dict = {}
            for i in page:
                # print(i.text)
                l.append(i.text)

            # print(type(l[3]))
            # # print(len(l))
            # if l[3]== None:
            #     continue
            # print(l[3])
            daily_record_dict['Name'] = (l[1])
            daily_record_dict['Measurement'] = l[2]
            daily_record_dict['Total_onion'] = int(l[3])
            daily_record_dict['Minimum_rate'] = int(''.join(filter(lambda i: i.isdigit(), l[4])))
            daily_record_dict['Maximum_rate'] = int(''.join(filter(lambda i: i.isdigit(), l[5])))
            daily_record_dict['Date'] = date
            print(daily_record_dict)
            # print(daily_record_dict)
            all_record_list.append(daily_record_dict)
    
       

        except AttributeError as e: #if not rates no available for url
            print(repr(e))
            continue
        except ValueError as e:
            print(repr(e))
            continue
    return all_record_list
if __name__ =='__main__':

    print(all_rates_function())

