import time
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import json
from itertools import islice
from reclamos import *
import MySQLdb
from datetime import datetime


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
        aux = soup.find("span", {"property": "v:dtreviewed"}).text
        date = datetime.strptime(aux.split(' ',1)[1], "%d, %B %Y")
        return date
    except:
        error = 'Fecha reclamo no encontrada, url {}'.format(url)
        write_error(error, path_err)
        return ''


def getDate_consulta(soup, url):
    try:
        aux = soup.find("div", {"class": "date"}).text
        date = datetime.strptime(aux.split(' ',1)[1], "%d, %B %Y")
        return date
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
        aux = soup.find('span', {'class':"cantidad-visitas"}).text
        visitas = int(aux.split()[0])
        return visitas
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


def loadNlines(file_opened, N):
    return [x.strip() for x in islice(file_opened, N)]


def writeNjson(reclamos, path_out):
    with open(path_out, "a") as outfile:
        for rec in reclamos:
            data = rec2json(rec)
            json.dump(data, outfile)
            outfile.write('\n')


def getURL(url):
    try:
        resp = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(resp, 'html.parser')
    except urllib.error.HTTPError as err:
        error = 'Error {} , url {}'.format(err.code, url)
        write_error(error)
        soup = None
    except ValueError:
        error = 'Error: Invalid URL {}'.format(url)
        write_error(error)
        soup = None
    return soup


def dbconnect(host, user, passwd, db):
    db = MySQLdb.connect(host=host,
                     user=user,
                     passwd=passwd,
                     db=db)
    cursor = db.cursor()
    return cursor


def proReclamo(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    if html != None:
        reclamo = getReclamo(soup, url)
        if reclamo == '': return None
        title = getTitle(soup, url)
        description = getDescription(soup, url)
        keywords = getKeywords(soup, url)
        itemreview = getItemreview(soup, url)
        summary = getSummary(soup, url)
        date_reclamo = getDate_reclamo(soup, url)
        #date_consulta = getDate_consulta(soup, url)
        ip_info = getIP_info(soup, url)
        state_rec = getState_rec(soup, url)
        ip_user = getIP_user(soup, url)
        visitas = getVisitas(soup, url)
        campo_empresa = getCampoEmpresa(soup, url)
        empresa = getEmpresa(soup, url)
        reclamo_i = reclamos(title, description, keywords, itemreview, summary, date_reclamo, ip_info, state_rec, reclamo, ip_info, visitas, campo_empresa, empresa)
        return reclamo_i
    return None