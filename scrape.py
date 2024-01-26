from requests import get
from bs4 import BeautifulSoup
from icecream import ic

URL= 'https://news.ycombinator.com/'

res = get(URL)
soup = BeautifulSoup(res.content,'html.parser')

links = soup.select('.titleline > a')
ic(links)
