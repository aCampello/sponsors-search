import os

import requests
from bs4 import BeautifulSoup


def get_data(path ='.'):
    r = requests.get('https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers')

    html = BeautifulSoup(r.content)

    doc_links = [x for x in html.findAll('a') if '.pdf' in x.attrs.get('href', '').lower()]

    r = requests.get(doc_links[-1].attrs.get('href'))

    with open(os.path.join(path, 'sponsors.pdf'), 'wb') as f:
        f.write(r.content)


if __name__ == "__main__":
    get_data()
