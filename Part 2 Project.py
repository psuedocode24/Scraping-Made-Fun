
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm as tqdm

import requests

import time

header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}



url  = 'https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=40&page=1'
page = requests.get(url, headers = header)


soup = BeautifulSoup(page.text, "html.parser")



def saveString(html, filename="text.html"):
	try:
		file = open(filename,"w")
		file.write(str(html))
		file.close()
	except Exception as ex:
		print('Error: ' + str(ex))
saveString(soup, 'bn_top100_01.html')        



def loadString(f="test.html"):
	try:
		html = open(f, "r", encoding='utf-8').read()
		return(html)
	except Exception as ex:
		print('Error: ' + str(ex))



prefix = "https://www.barnesandnoble.com"
book_title = soup.findAll('h3', class_ = 'product-info-title')
for i,book in enumerate(book_title):
#     print('The Book Title":', book.text)
    book_link = book.find('a')['href']
    book_link = prefix + book_link
#     print('Book link:', book_link)
    time.sleep(5)
    book_page = requests.get(book_link, headers = header)
    soup = saveString(book_page.text, f'bn_top100_{i}.html')




for i,book in enumerate(book_title):
    soup = loadString(f'bn_top100_{i}.html')
    soup = BeautifulSoup(soup, "html.parser")
    booktitle = soup.find('h1', class_ = 'pdp-header-title text-lg-left text-sm-center mr-md-l ml-md-l mr-sm-l ml-sm-l')
    print("Title: ",booktitle.text)
    overview = soup.find('div', class_ = 'overview-cntnt')
    print("Overview: ", overview.text[:100])

