from utils import *
import MySQLdb as mdb


def main():
    file_urls = '../../urls_reclamos.csv'
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


def main_html2json():
    path_out = '../data/reclamos_cl.json'
    batch_size = 1024


    cursor = dbconnect(host="localhost",
                     user="ribanez",
                     passwd="abc123",
                     db="RECLAMOS")

    count = 309042 # cursor.execute(SELECT COUNT(*) FROM html)
    for offset in range(0, count, batch_size):
        
        cursor.execute("SELECT url, html FROM html LIMIT %s OFFSET %s",(batch_size, offset))
        
        rec_batch = []
        for row in cursor.fetchall():
            url = row[0]
            html = row[1]
            reclamoi = proReclamo(html, url)
        #print(html)
        #print(url)
            if reclamoi != None: rec_batch.append(reclamoi) 
        writeNjson(rec_batch, path_out)
        print('Se han leido {}/{}'.format(offset+batch_size,count))
    print('Base de datos leida con éxito!')


def main_html2db():
    data_base_exist = False
    batch_size = 512
    DB_HOST = 'localhost'
    DB_USER = 'ribanez'
    DB_PASSWORD = 'abc123'
    DB_NAME = 'RECLAMOS_RAW'


    cursor = dbconnect(host="localhost",
                     user="ribanez",
                     passwd="abc123",
                     db="RECLAMOS")

    con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor2 = con.cursor()

    if not data_base_exist: create_sql(cursor2)

    count = 309042 # cursor.execute(SELECT COUNT(*) FROM html)
    for offset in range(0, count, batch_size):
        
        cursor.execute("SELECT url, html FROM html LIMIT %s OFFSET %s",(batch_size, offset))


        for row in cursor.fetchall():
            url = row[0]
            html = row[1]
            reclamoi = proReclamo(html, url)

            #if reclamoi != None:
                #populate_sql(cursor2, rec, url)

        print('Se han leido {}/{}'.format(offset+batch_size,count))
    print('Base de datos leida con éxito!')


def printSchemaTable(cursor):
    cursor.execute("desc html")
    print([column[0] for column in cursor.fetchall()])
    


if __name__ == '__main__':
    main_html2json()
