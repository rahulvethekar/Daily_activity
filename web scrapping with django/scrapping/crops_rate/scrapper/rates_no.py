from bs4 import BeautifulSoup
import requests

def updated_rates_no():
    source = requests.get('http://www.puneapmc.org/rates.aspx')
    soup = BeautifulSoup(source.content,'html.parser')
    td = soup.find('td', class_ ='main_body')
    uls = td.find_all('ul')
    lists = uls[1]
    link=lists.find('li').a.get('href')
    no  = ''
    for i in link:
        if  i.isdigit():
            no = no + i

    print(no)
    return int(no)
if __name__=='__main__':
    updated_rates_no()



