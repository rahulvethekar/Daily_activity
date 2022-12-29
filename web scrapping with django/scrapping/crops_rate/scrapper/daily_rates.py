from bs4 import BeautifulSoup
import requests

def daily_rates_function():
    source = requests.get('http://www.puneapmc.org/rates.aspx?page=rates&catid=1')
    soup = BeautifulSoup(source.content,'html.parser')
    page = soup.find('tr',class_='tr1').find_all('td')
    date_tag = soup.find('td',class_='main_body').find('h1')
    date = date_tag.text.split('-')[1]

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

