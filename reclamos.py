import time
from bs4 import BeautifulSoup
import requests


def main():
    f = open('../urls_reclamos.csv')
    for line in f:
        line = line.replace('"', '')
        url = line.replace('\n','')
        if url == 'url':
            pass
        else:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            print(soup.prettify())
            time.sleep(10)


if __name__ == '__main__':
    main()
