from bs4 import BeautifulSoup
import requests

source = requests.get('https://mojok.co/').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.div.h1.text
    print(headline)

    summary = article.find('span', class_='cb-itemprop').p.text
    print(summary)

    print()