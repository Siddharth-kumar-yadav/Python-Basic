import requests
from bs4 import BeautifulSoup

# with open("sample.html","r") as f:
#     html_doc = f.read()

proxies = { # write your own proxy at here
  "http": "http://",
  "https": "https:",
}


# r= requests.get("https://api.ipify.org?format=json")
# print(r.json())

url ="https://www.amazon.in/s?k=iphone&crid=1F6XH3S6LTAAS&sprefix=iph%2Caps%2C260&ref=nb_sb_ss_pltr-data-refreshed_2_3"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
# spans =soup.find(class_="a-page")
# print(spans)

spans =soup.select("span.a-size-mini a-spacing-none a-color-base s-line-clamp-2")
prices = soup.select("span.a-price")
for span in spans:
    print(span.string)

for price in prices:
    print(price.string)    