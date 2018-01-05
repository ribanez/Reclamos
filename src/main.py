from utils import *


def main():
    file_urls = '../../urls_reclamos.csv'

    path_out = '../data/reclamos_raw.json'
    n_batch = 84

    with open(file_urls) as f:
        lines = loadNlines(f, n_batch)
        rec_batch = []
        for line in lines:
            line = line.replace('"', '')
            url = line.replace('\n','')
            soup = getURL(url)
            reclamoi = proReclamo(soup, url)
            if reclamoi != None: rec_batch.append(reclamoi) 
        writeNjson(rec_batch, path_out)
    print('\n urls recorridas con éxito \n')


if __name__ == '__main__':
    main()
