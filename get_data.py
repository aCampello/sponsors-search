import requests
r = requests.get('https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers')

from bs4 import BeautifulSoup

html = BeautifulSoup(r.content)

doc_links = [x for x in html.findAll('a') if 'tier_2_5' in x.attrs.get('href', '').lower()]

r = requests.get(doc_links[-1].attrs.get('href'))

with open('sponsors.pdf', 'wb') as f:
    f.write(r.content)
