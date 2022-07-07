import mysql.connector
from mysql.connector import errorcode

def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='gestaoprof')
        print('Conectado ao Banco de dados')
        return db_connection

    except mysql.connector.Error as erro:
        if erro.errno == errorcode.ER_BAD_DB_ERROR:  #banco de dados não existe
            print('Banco de dados não existe!, {}'.format(erro))
        elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:  #usuário ou senha errados
            print('Usuário ou senha não são válidos!, {}'.format(erro))
        else:
            print(erro)

    else:
        db_connection.close()