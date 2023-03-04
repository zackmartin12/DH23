import requests
from bs4 import BeautifulSoup

url = 'https://www.dickssportinggoods.com/f/mens-sale-apparel'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

deals = soup.find_all('div', {'class':'deal-item'})

for deal in deals:
    title = deal.find('h3', {'class':'title'}).text
    print(title)
