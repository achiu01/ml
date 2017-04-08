from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#read url and parse
url = "http://www.bloomberg.com/quote/SPX:IND"
page_soup = soup(uReq(url).read(), 'html.parser')
#print(page_soup.h1)

# Take out the <div> of name and get its value
name_box = page_soup.find('h1', attrs={'class': 'name'})
print(name_box)

# strip() is used to remove starting and trailing
name = name_box.text.strip()

print(name)

# get the index price
price_box = page_soup.find('div', attrs={'class':'price'})
price = price_box.text
print(price)
