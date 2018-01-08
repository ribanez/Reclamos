import sqlite3
from utils import *


conn = sqlite3.connect('RECLAMOS_CL')
curs = conn.cursor()


def create_table():
    curs.execute('''drop table if exists reclamos_cl''')
    curs.execute('''create table reclamos_cl (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 url text,
                 title text,
                 description text,
                 keywords text,
                 itemreview text,
                 summary text,
                 date_reclamo date,
                 ip_user text,
                 visitas integer,
                 campo_empresa text,
                 empresa text,
                 reclamo text
                );''')
    conn.commit()


def populate_table(rec, url):
    
    row = (None, url, rec.title, rec.description, rec.keywords, rec.itemreview, rec.summary, rec.date_reclamo, rec.ip_user, rec.visitas, rec.campo_empresa, rec.empresa, rec.reclamo)

    curs.execute('insert into reclamos_cl values (?,?,?,?,?,?,?,?,?,?,?,?,?);', row)
    conn.commit()


def table2dump():
    with open('../data/RECLAMOS_CL_dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)


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

    create_table()

    count = 309042 # cursor.execute(SELECT COUNT(*) FROM html)
    for offset in range(0, count, batch_size):
        
        cursor.execute("SELECT url, html FROM html LIMIT %s OFFSET %s",(batch_size, offset))


        for row in cursor.fetchall():
            url = row[0]
            html = row[1]
            reclamoi = proReclamo(html, url)

            if reclamoi != None:
                populate_table(reclamoi, url)

        print('Se han leido {}/{}'.format(offset+batch_size,count))
    print('Base de datas leida con éxito!')
    print('/n ---- TABLE TO DUMP ------ /n')
    table2dump()



if __name__ == '__main__':
    main_html2db()