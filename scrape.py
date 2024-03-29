import requests
from bs4 import BeautifulSoup
import pprint

# get the page
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# parse the page
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

# combine the pages
links.extend(links2)
subtext.extend(subtext2)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        link = item.select_one('a')
        href = link.get('href', None)  # none is default value
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
