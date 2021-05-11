import pymysql
def conectar():
    miConexion = pymysql.connect( host='localhost', user= 'asiracor_root', passwd='toor12345', db='determinantes' )
    return miConexion