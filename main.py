from reclamos import *
from utils import *


def main():
    f = open('../urls_reclamos.csv')
    for line in f:
        line = line.replace('"', '')
        url = line.replace('\n','')
        if url == 'url':
            soup = None
        else:
            resp = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(resp, 'html.parser')
        
        if soup != None:
            title = getTitle(soup)
            description = getDescription(soup)
            keywords = getKeywords(soup)
            itemreview = getItemreview(soup)
            summary = getSummary(soup)
            date_reclamo = getDate_reclamo(soup)
            #date_consulta = getDate_consulta(soup)
            ip_info = getIP_info(soup)
            state_rec = getState_rec(soup)
            reclamo = getReclamo(soup)
            ip_user = getIP_user(soup)
            visitas = getVisitas(soup)
        
            reclamo_i = reclamos(title, description, keywords, itemreview,
                                 summary, date_reclamo, ip_info, state_rec,
                                 reclamo, ip_info, visitas)

            #print(reclamo_i.reclamo)

    print('\n urls recorridas con éxito \n')


if __name__ == '__main__':
    main()
