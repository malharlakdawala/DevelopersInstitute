import requests
from bs4 import BeautifulSoup
import time

store = []

def multiple_requests():
    for i in range(1, 3):  #get response from multiple pages
        parameters = {'q': i}
        response = requests.get('https://news.ycombinator.com/news', params=parameters)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.select('.titlelink')
        subtext = soup.select('.subtext')
        extract_info(links, subtext)
        time.sleep(10)


def extract_info(links, subtext):
    for index in range(len(links)):
        value = links[index].getText()
        href = links[index].get('href', None)
        points = subtext[index].select('.score')
        if len(points) > 0:
            if "points" in points[0].getText():
                points = int(points[0].getText().replace(' points', ''))
            else:
                points = int(points[0].getText().replace(' point', ''))
            if points > 99:
                store.append({'title': value, 'link': href, 'votes': points})

multiple_requests()
print(store)
