# Dump Base de Datos SQL

## Pasos previos

### Actualizar Linux

Abrir una terminal ( *ctrl + alt + t* ) y ejecutar los siguientes comandos

```
sudo apt update
sudo apt dist-upgrade
```

### Instalar MySQL (server y client - just in case)

No le asigné un pass

```
sudo apt install mysql-server
sudo apt install mysql-client
```

### Verificar que MySQL esté ejecutándose

```
sudo service mysql status
```

## Crear Base de Datos
### Entrar a shell de MySQL

```
sudo mysql
```

Una vez dentro de la shell se verá 

```
mysql>
```


### Crear database con nombre RECLAMOS

```
mysql> create database RECLAMOS;
```


### Salir de shell de MySQL
Usar el comando de teclas *'ctrl + d'*, o bien escribir *'exit'*

```
mysql> exit
```


## DUMP

Desde la terminal, hacer dump desde el archivo *SQL* (*reclamos.cl.sql*) a la base de datos creada anteriormente (*RECLAMOS*)


```
mysql -u root -p RECLAMOS < reclamos.cl.sql
```

## Crear usuario y modificar permisos de usuario

En mi caso, el usuario es: `diego` y no defino un password.

En caso de definir un password, modificar el string vacío `''` luego de `'IDENTIFIED BY'`


```
sudo mysql

mysql> CREATE USER 'diego'@'localhost' IDENTIFIED BY '';

mysql> GRANT ALL ON *.* TO 'diego'@'localhost';

mysql> exit
```


### Verificar que se creó correctamente el usuario

Si te permite ingresar a la shell de *MySQL*, verificas que se creó correctamente (para el password, presionar enter)

```
mysql -u diego -p
mysql> 
```

## Instalar MySQLdb

Para manipular la base de datos desde *Python3*, se debe instalar *MySQLdb*

```
sudo apt install -y python3-mysqldb --upgrade
```

# Script básico (Ejemplo)

Abrir una terminal y entrar a la consola de *Python3*

```
python3

>>>
```

Una vez abierta la consola de *Python*, ejecutar el siguiente script, el cuál imprime en pantalla las *URLs* leídas desde la base de datos *SQL* utilizando *MySQLdb*.

```
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="diego",
                     passwd="",
                     db="RECLAMOS")

cur = db.cursor()

cur.execute("SELECT url FROM  html")

for row in cur.fetchall():
    url = row[0]
    print(url)
```

