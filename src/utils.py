import time
from bs4 import BeautifulSoup
import urllib.request
import re
import csv


def getTitle(soup):
   try:
      return soup.title.string
   except:
      print('Título no encontrado')
      return ''


def getDescription(soup):
    try:
        return soup.find('meta', {'name':'description'})['content']
    except:
        print('Descripcion no encontrada')
        return ''


def getKeywords(soup):
    try:
        return soup.find('meta', {'name':'keywords'})['content']
    except:
         print('Keywords no encontradas')
         return ''


def getItemreview(soup):
    try:
        return soup.find('span', {'property':'v:itemreviewed'}).text
    except:
        print('Itemviewed no encontrado')
        return ''


def getSummary(soup):
    try:
        return soup.find('span', {'property':'v:summary'}).text
    except:
        print('Resumen no encontrado')
        return ''


def getDate_reclamo(soup):
    try:
        return soup.find("span", {"property": "v:dtreviewed"}).text
    except:
        print('Fecha reclamo no encontrada')
        return ''


def getDate_consulta(soup):
    try:
        return soup.find("div", {"class": "date"}).text
    except:
        print('Fecha consulta no encontrada')
        return ''


def getIP_info(soup):
    try:
        return soup.find('div', {'class':"reclamo-meta-autor"}).text
    except:
        print('IP Autor no encontrado')
        return ''


def getState_rec(soup):
    try:
        return soup.find("div", {"class": "content"}).text
    except:
        print('Estado de reclamo no encontrado')
        return ''


def getReclamo(soup):
    try:
        return soup.find('span', {'property':"v:description"}).text
    except:
        print('Reclamo no encontrado')
        return ''


def getIP_user(soup):
    try:
        ips =  soup.find('div', {'class':"reclamo-meta-autor"}).text
        return re.findall( r'[0-9]+(?:\.[0-9]+){3}', ips )
    except:
        print('IP user no encontrada')
        return ''


def getVisitas(soup):
    try:
        return soup.find('span', {'class':"cantidad-visitas"}).text
    except:
        print('No se encontró el numero de visitas')
        return ''


def writeCSV(reclamo, path_out):

    line = reclamo.title + '\t' + reclamo.description + '\t' + reclamo.keywords + '\t' + reclamo.itemreview +'\t' + reclamo.summary + '\t' + reclamo.date_reclamo + '\t' +  reclamo.ip_info +'\t' +reclamo.state_rec + '\t' + reclamo.reclamo + '\t' + reclamo.ip_user + '\t' + reclamo.visitas + '\n'

    with open(path_out, "a") as csv_file:
        csv_file.write(line)
