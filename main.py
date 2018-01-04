import time
from bs4 import BeautifulSoup
import urllib.request
import re
from reclamos import *


def main():
    f = open('../urls_reclamos.csv')
    for line in f:
        line = line.replace('"', '')
        url = line.replace('\n','')
        if url == 'url':
            pass
        else:
            resp = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(resp, 'html.parser')

            try:
                title = soup.title.string
            except:
                print('Título no encontrado')
                title = ''

            try:
                description = soup.find('meta', {'name':'description'})['content']
            except:
                print('Descripcion no encontrada')
                description = ''

            try:
                keywords = soup.find('meta', {'name':'keywords'})['content']
            except:
                print('Keywords no encontradas')
                keywords = ''

            try:
                itemreview = soup.find('span', {'property':'v:itemreviewed'}).text
            except:
                print('Itemviewed no encontrado')
                itemreview = ''

            try:
                summary = soup.find('span', {'property':'v:summary'}).text
            except:
                print('Resumen no encontrado')
                summary = ''

            try:
                date_reclamo = soup.find("span", {"property": "v:dtreviewed"}).text
            except:
                print('Fecha reclamo no encontrada')
                date_reclamo = ''

            try:
                date_consulta = soup.find("div", {"class": "date"}).text
            except:
                print('Fecha consulta no encontrada')
                date_consulta = ''

            try:
                ip_autor = soup.find('div', {'class':"reclamo-meta-autor"}).text
            except:
                print('IP Autor no encontrado')
                ip_autor = ''

            try:
                state_rec = soup.find("div", {"class": "content"}).text
            except:
                print('Estado de reclamo no encontrado')
                state_rec = ''

            try:
                reclamo = soup.find('span', {'property':"v:description"}).text
            except:
                print('Reclamo no encontrado')
                reclamo = ''

            try:
                ips = soup.find('div', {'class':"reclamo-meta-autor"}).text
                ip_user = re.findall( r'[0-9]+(?:\.[0-9]+){3}', ips )
            except:
                print('IP user no encontrada')
                ip_user = ''


            try:
                visitas = soup.find('span', {'class':"cantidad-visitas"}).text
            except:
                print('No se encontró el numero de visitas')
                visitas = ''


            reclamo_i = reclamos(title, description, keywords, itemreview,
                                 summary, date_reclamo, date_consulta,
                                 ip_autor, state_rec, reclamo, ip_user,
                                 visitas)

            print(reclamo_i.reclamo)


            #time.sleep(1)


if __name__ == '__main__':
    main()
