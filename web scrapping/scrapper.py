from bs4 import BeautifulSoup
import requests

# source = requests.get('https://www.questionsanswered.net/article/how-read-newspaper-articles-online?utm_content=params%3Ao%3D740012%26ad%3DdirN%26qo%3DserpIndex&ueid=afc1e795-3b5d-4662-9585-3534011a24a4')
# print(source)
source = requests.get('http://www.puneapmc.org/rates.aspx')
soup = BeautifulSoup(source.content,'html.parser')

page = soup.find('td',class_='main_body').find('h1')
print(page.text)

page = soup.find('td',class_='main_body').find('ul').find_all('li')
for i in page:
    print(i.a.get('href')
    )

