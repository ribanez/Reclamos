import MySQLdb


def main():

    # Editar Datos  del Connect según sea el caso

    db = MySQLdb.connect(host="localhost",
                         user=user,
                         passwd="",
                         db="RECLAMOS")

    cur = db.cursor()

    cur.execute("SELECT url FROM  html")

    count = 0

    for row in cur.fetchall():

        url = row[0]

        with open('urls.csv', 'a') as file:

        # OJO:
        #  'a' : append
        # Verificar que el archivo no exista y ejecutar el codigo 1 sola vez

            if count == 0:
                file.write('url' + '\n')
                count += 1
            else:
                file.write(url + '\n')

        file.close()


if __name__ == '__main__':
    main()
