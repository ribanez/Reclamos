import time
from bs4 import BeautifulSoup
import urllib.request
import re
import csv

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


def writeCSV(reclamo, path_out):

    line = reclamo.title + '\t' + reclamo.description + '\t' + reclamo.keywords + '\t' + reclamo.itemreview +'\t' + reclamo.summary + '\t' + reclamo.date_reclamo + '\t' +  reclamo.ip_info +'\t' +reclamo.state_rec + '\t' + reclamo.reclamo + '\t' + reclamo.ip_user + '\t' + reclamo.visitas + '\t' + reclamo.campo_empresa + '\t' + reclamo.empresa + '\n'

    with open(path_out, "a") as csv_file:
        csv_file.write(line)


def loadCSV(path_in):
    with open(path_in, "rb") as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
             yield line


def write_error(error, path_file = path_err ):
    with open(path_file, "a") as f:
        f.write(error + '\n')
