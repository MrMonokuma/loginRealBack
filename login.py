#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi

datos = cgi.FieldStorage()

print('Content-Type: text/html')
print('')

try:
    cnx = mysql.connector.connect(user='nicolasdb', password ='Nicolas@!26', database='dbprueba', host='127.0.0.1')
    cursor = cnx.cursor()
    print('Conectado')
    usuario = datos.getvalue('usr')
    contraseña = datos.getvalue('pass')

    add_usr = ("INSERT INTO usuarios "
               "(username, contraseña) "
               "VALUES (%s, SHA(%s))")
    data_usr = (usuario, contraseña)
    cursor.execute(add_usr, data_usr)
    print('Añadiendo')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

cnx.commit()
cursor.close()
cnx.close()



