import mysql.connector
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(host='localhost',user='root',password='',database='estoque')
    print("Database connection made!")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe!")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário e ou senha está incorreto!")
    else: 
        print(error)
