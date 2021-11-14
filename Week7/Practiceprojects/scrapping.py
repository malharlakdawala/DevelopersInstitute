import requests
from bs4 import BeautifulSoup

response =requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text,'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

def extract_info(links,subtext):
    store=[]
    for index in range(len(links)):
        value = links[index].getText()
        href=links[index].get('href', None)
        points = subtext[index].select('.score')
        if len(points)>0:
            if "points" in points[0].getText():
                points= int(points[0].getText().replace(' points',''))
            else: points= int(points[0].getText().replace(' point',''))
            if points>99:
                store.append({'title':value, 'link':href, 'votes':points})
    return store

print(extract_info(links,subtext))

