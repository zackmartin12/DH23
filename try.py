from bs4 import BeautifulSoup
import requests

url = 'https://twothirds.com/en-us/collections/sale-men'

result = requests.get(url)
# print(result.text)
doc = BeautifulSoup(result.text, "html.parser")
tags = doc.find("title")
# print(doc.prettify())
print(tags.string)