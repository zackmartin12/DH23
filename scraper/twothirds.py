import requests
from bs4 import BeautifulSoup

url = 'https://www.twothirds.com/en-us/collections/sale-men'
page = requests.get(url).text
doc = BeautifulSoup(page, 'html.parser')

title = doc.find('title').text
print(title)



