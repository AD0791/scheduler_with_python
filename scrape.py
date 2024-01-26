from requests import get
from bs4 import BeautifulSoup
from icecream import ic
from schedule import run_pending, every, repeat
import time

@repeat(every(0.5).minutes,  n=3)
def get_articles_from_ycombinator(n:int)->list[dict]:
    URL= 'https://news.ycombinator.com/'
    res = get(URL)
    soup = BeautifulSoup(res.content,'html.parser')
    data = list()
    links = soup.select('.titleline > a')
    scores = soup.select('.score')
    for link, score in zip(links , scores):
        details = dict()
        details['article_name'] = link.text
        details['article_url'] = link.attrs['href']
        details['article_score'] = int(score.text.split()[0])
        data.append(details)
    data = sorted(data,key=lambda x: x['article_score'], reverse=True)[:n]
    ic('--------------------')
    ic(data)
    return data



####### schedulers

while True:
    run_pending()
    time.sleep(1)
