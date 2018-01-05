import time
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import json


path_err = '../data/errores.log'

def getTitle(soup, url):
   try:
      return soup.title.string 
   except:
      error = 'Título no encontrado, url {}'.format(url)
      write_error(error, path_err)
      return ''


def getDescription(soup, url):
    try:
        return soup.find('meta', {'name':'description'})['content']
    except:
        error = 'Descripcion no encontrada, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getKeywords(soup, url):
    try:
        return soup.find('meta', {'name':'keywords'})['content']
    except:
         error = 'Keywords no encontradas, url {}'.format(url)
         write_error(error, path_err)
         return ''


def getItemreview(soup, url):
    try:
        return soup.find('span', {'property':'v:itemreviewed'}).text
    except:
        error = 'Itemviewed no encontrado, url {}'.format(url) 
        write_error(error, path_err)
        return ''


def getSummary(soup, url):
    try:
        return soup.find('span', {'property':'v:summary'}).text
    except:
        error = 'Resumen no encontrado, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getDate_reclamo(soup, url):
    try:
        return soup.find("span", {"property": "v:dtreviewed"}).text
    except:
        error = 'Fecha reclamo no encontrada, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getDate_consulta(soup, url):
    try:
        return soup.find("div", {"class": "date"}).text
    except:
        error = 'Fecha consulta no encontrada, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getIP_info(soup, url):
    try:
        return soup.find('div', {'class':"reclamo-meta-autor"}).text
    except:
        error = 'IP Autor no encontrado, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getState_rec(soup, url):
    try:
        return soup.find("div", {"class": "content"}).text
    except:
        error = 'Estado de reclamo no encontrado, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getReclamo(soup, url):
    try:
        return soup.find('span', {'property':"v:description"}).text
    except:
        error = 'Reclamo no encontrado, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getIP_user(soup, url):
    try:
        ips =  soup.find('div', {'class':"reclamo-meta-autor"}).text
        return re.findall( r'[0-9]+(?:\.[0-9]+){3}', ips )
    except:
        error = 'IP user no encontrada, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getVisitas(soup, url):
    try:
        return soup.find('span', {'class':"cantidad-visitas"}).text
    except:
        error = 'No se encontró el numero de visitas, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getCampoEmpresa(soup, url):
    try:
        return soup.find('div', {'class':"breadcrumb"}).find_all('a', href=True, text=True)[1].text
    except:
        error = 'No se encontró campo empresa, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getEmpresa(soup, url):
    try:
        return soup.find('div', {'class':"breadcrumb"}).find_all('a', href=True, text=True)[2].text
    except:
        error = 'No se encontró empresa, url {}'.format(url)
        write_error(error, path_err)
        return ''


def rec2json(reclamo):
   data = {"Reclamo" : [ { "title":reclamo.title, "description":reclamo.description, "keywords":reclamo.keywords, "itemreview":reclamo.itemreview, "summary":reclamo.summary, "date_reclamo":reclamo.date_reclamo, "ip_info":reclamo.ip_info, "state_rec":reclamo.state_rec, "reclamo":reclamo.reclamo, "ip_user":reclamo.ip_user, "visitas":reclamo.visitas, "campo_empresa":reclamo.campo_empresa, "empresa":reclamo.empresa } ] }
   return data


def write_error(error, path_file = path_err ):
    with open(path_file, "a") as f:
        f.write(error + '\n')


def writeJson(reclamo, path_out): 
    data = rec2json(reclamo)
    with open(path_out, 'a') as outfile:
        json.dump(data, outfile)