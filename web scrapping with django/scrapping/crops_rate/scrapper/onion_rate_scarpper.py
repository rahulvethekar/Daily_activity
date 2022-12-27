from bs4 import BeautifulSoup
import requests

def onion_rate_scrapper():
    source = requests.get('http://www.puneapmc.org/rates.aspx')
    soup = BeautifulSoup(source.content,'html.parser')
    page = soup.find('td',class_='main_body').find('ul')
    ul = page.next_sibling.next_sibling.next_sibling
    # data = {}
    records = []
    for li in ul.find_all('li'):
        print(li.text)
        # data[li.text.replace('View Rates','')] = li.a.get('href')
        records.append({'Date':li.text.replace('- View Rates',''),'link':li.a.get('href')})
    print(records)
    
        


    # for records in page.find:
    #     print(records.li)
    #     print('-----')
    # data = {}
    # for i in page.find_all('li'):
    #     print(i.a.get('href'))
    #     data[(i.a.text)] = i.a.get('href')
    # return data
    
