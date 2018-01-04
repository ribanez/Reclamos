from reclamos import *
from utils import *


def main():
    f = open('../../urls_reclamos.csv')

    path_out_csv = '../data/reclamos_raw.csv'
    header = reclamos('title', 'description', 'keywords', 'itemreview', 'summary', 'date_reclamo', 'ip_info', 'state_rec', 'reclamo', 'ip_user', 'visitas', 'campo_empresa', 'empresa')
    writeCSV(header, path_out_csv)

    for line in f:
        line = line.replace('"', '')
        url = line.replace('\n','')

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
        
        if soup != None:
            title = getTitle(soup, url)
            description = getDescription(soup, url)
            keywords = getKeywords(soup, url)
            itemreview = getItemreview(soup, url)
            summary = getSummary(soup, url)
            date_reclamo = getDate_reclamo(soup, url)
            #date_consulta = getDate_consulta(soup, url)
            ip_info = getIP_info(soup, url)
            state_rec = getState_rec(soup, url)
            reclamo = getReclamo(soup, url)
            ip_user = getIP_user(soup, url)
            visitas = getVisitas(soup, url)
            campo_empresa = getCampoEmpresa(soup, url)
            empresa = getEmpresa(soup, url)

            reclamo_i = reclamos(title, description, keywords, itemreview,
                                 summary, date_reclamo, ip_info, state_rec,
                                 reclamo, ip_info, visitas, campo_empresa, empresa)

            
            writeCSV(reclamo_i, path_out_csv)

    print('\n urls recorridas con éxito \n')


if __name__ == '__main__':
    main()
