from bs4 import BeautifulSoup
import requests
import time
def all_rates_function():
    for no in range(2480,3292+1):
        try:
            source = requests.get('http://www.puneapmc.org/history.aspx?id=Rates'+str(no))
            soup = BeautifulSoup(source.content,'html.parser')
            page = soup.find('tr',class_='tr0').find_all('td')
            print(no)
            # date_tag = soup.find('td',class_='main_body').find('h1')
            # date = date_tag.text.split('-')[1]

            print(page)
            l = []
            daily_record_dict = {}
            for i in page:
                # print(i.text)
                l.append(i.text)

            print(l)
            if not l[3]==str:
                continue
            all_record_list = []
            daily_record_dict['Name'] = (l[1])
            daily_record_dict['Measurement'] = l[2]
            daily_record_dict['Total_onion'] = int(l[3])
            daily_record_dict['Minimum_rate'] = int(''.join(filter(lambda i: i.isdigit(), l[4])))
            daily_record_dict['Maximum_rate'] = int(''.join(filter(lambda i: i.isdigit(), l[5])))
            print(daily_record_dict)
            # print(daily_record_dict)
            all_record_list.append(daily_record_dict)
    
       

        except AttributeError:
            continue
        print(all_record_list)

    return daily_record_dict
if __name__ =='__main__':

    all_rates_function()

