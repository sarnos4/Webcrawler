import requests
from bs4 import BeautifulSoup

def book_spider(max_page):
    page = 1
    while page <= max_page:

        url = 'https://www.barnesandnoble.com/b/books/biography/_/N-1fZ29Z8q8Zsoc?Ns=P_Sales_Rank'+ str(page)
        #sets request to grab HTTP url
        results = requests.get(url)
        #stores HTTP as readable code in source_text
        source_text = results.text
        #BSoup pulls data from html/xml files, stores in bs_data
        bs_data = BeautifulSoup(source_text, 'html.parser')
        #loop scans through data, looking for any html class ' '
        for link in bs_data.findAll('a', {'class':' '}):
            #href prints full url for access
            href = 'https://www.barnesandnoble.com'+link.get('href')
            #calls function to print title&price
            get_href_data(href)
            #prints usuable link
            print(href)

        page += 1

#function accesses each href, pulls title & price in for loops
def get_href_data(post_url):
    results = requests.get(post_url)
    source_text = results.text
    bs_data = BeautifulSoup(source_text, 'html.parser')
    for book_title in bs_data.findAll('h1', {'itemprop': 'name'}):
        print(book_title.string)
    for book_price in bs_data.findAll('s', {'class': 'old-price'}):
        print(book_price.string)


book_spider(1)
