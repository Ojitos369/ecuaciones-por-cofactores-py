from src.extras import clean, convert_float, pause
from conexion import conectar
import pymysql as mysql
import json
import time
import random
import sys

encontradas_en_db = 0
donde = []
iguales = 0
encontradas = 0
no_encontradas = 0
conexion = conectar()
cur = conexion.cursor()
determinantes_no_encontradas = {}
""" try:
    clean()
    print('Iniciando...')
    with open('determinantes.json', 'r') as f:
        diccionario_de_determinantes = json.load(f)
    clean()
except:
    diccionario_de_determinantes = {} """

def contar_caracteres(cadena, caracter):
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            contador += 1
    return contador

def agregar(diccionario):
    i = 0
    print()
    datos_totales = len(diccionario) - 1
    for nombre, det in diccionario.items():
        n = contar_caracteres(nombre, '[') - 1
        crear_tabla(n)
        query = f"INSERT INTO det_{n}x{n} (nombre, determinante) VALUES ('{nombre}', {det});"
        #print(f'{i}.- "{query}"')
        sys.stdout.write("\033[F")
        print(f'Actualizando datos: {i}/{datos_totales} --- Faltan: {datos_totales - i} ')
        i += 1
        try:
            cur.execute(query)
        except:
            pass


def crear_tabla(n):
    query = f"""CREATE TABLE det_{n}x{n} (id INT(255) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(1000),
determinante VARCHAR(1000))"""
    try:
        cur.execute(query)
    except:
        pass

def imprimir_matriz(mat):
    try:
        filas = len(mat)
        columnas = len(mat[0])
    except:
        filas = 0
        columnas = 0
    for i in range(filas):
        for j in range(columnas):
            try:
                print(f'{mat[i][j]}', end='\t')
                if j == columnas-1: print()
            except:
                pass

def ingresar_matriz(filas, columnas, text=''):
    ma=[]
    for i in range(filas):
        ma.append([])
        for j in range(columnas):
            clean()
            print(f'{text}')
            imprimir_matriz(ma)
            numero = input(f'\nIngresa el numero de la posicion {i+1},{j+1}: ')
            numero = convert_float(numero)
            if numero:
                ma[i].append(numero)
            else:
                ma[i].append(0)
    clean()
    print('Matriz: ')
    imprimir_matriz(ma)
    pause()
    return ma

def determinante_base(mat):
    global determinantes_no_encontradas
    global encontradas
    global no_encontradas
    global encontradas_en_db
    global iguales
    longitud = len(mat)
    lon2 = len(mat[0])
    if longitud == 1:
        return mat[0][0]
    elif longitud == lon2:
        try:
            determinante = 0
            query = f"SELECT determinante FROM det_{longitud}x{longitud} WHERE nombre = '{mat}';"
            cur.execute(query)
            det = cur.fetchall()
            try:
                #print(f'determinante de base en {mat} : {det}')
                #pause()
                det = float(det[0][0])
                #print(f'Determinante despues de float: {det}')
                #print(f'Tomo de base de datos')
                encontradas_en_db += 1
            except:
                det = determinantes_no_encontradas[str(mat)]
                #print(f'Entro al diciconario en {mat}')
                iguales += 1
                #pause()
            encontradas += 1
            return det
        except:
            determinante = 0
            #print(f'Entro matriz {mat}')
            #pause()
            resultados_cofactores = []
            for i in range(longitud):
                matriz_auxiliar = []
                for j in range(longitud - 1):
                    matriz_auxiliar.append([])
                    for k in range(longitud - 1):
                        matriz_auxiliar[j].append(1)
                auxi=0
                for j in range(longitud - 1):
                    if j==i: auxi+=1
                    auxj=1
                    for k in range(longitud - 1):
                        matriz_auxiliar[j][k] = mat[j+auxi][k+auxj]
                a = mat[i][0]
                b = determinante_base(matriz_auxiliar)
                c = a * b
                resultados_cofactores.append(c)
            for i in range(len(resultados_cofactores)):
                if i % 2 == 0:
                    determinante += resultados_cofactores[i]
                else:
                    determinante -= resultados_cofactores[i]
                    
            determinantes_no_encontradas[str(mat)] = determinante
            no_encontradas += 1
            donde[longitud - 2] += 1
            return determinante

def solucion(datos, resultados):
    clean()
    filas = len(datos)
    res_long = len(resultados)
    columnas = len(datos[0])
    if filas == columnas and res_long == filas:
        inicio_de_tiempo = time.time()
        matrices = []
        determinantes = []
        determinante_original = determinante_base(datos)
        fin_de_tiempo = time.time()
        tiempo_determinante_original = fin_de_tiempo - inicio_de_tiempo
        if determinante_original != 0:
            longitud = len(datos)
            for i in range(longitud):
                matriz_auxiliar = []

                for elemento in datos:
                    matriz_auxiliar.append(elemento[:])

                for j in range(longitud):
                    matriz_auxiliar[j][i] = resultados[j][0]
                
                matrices.append(matriz_auxiliar)
                determinantes.append(determinante_base(matriz_auxiliar))
            fin_de_tiempo_total = time.time()
            tiempo_total = fin_de_tiempo_total - inicio_de_tiempo
            mostrar = True
            while mostrar:
                clean()
                print('Datos')
                imprimir_matriz(datos)
                print('Resultados')
                imprimir_matriz(resultados)
                for i in range(len(determinantes)):
                    resultado = round(determinantes[i]/determinante_original, 5)
                    print(f'El valor {i+1} es: {resultado}')
                print()
                print(f'Tiempo de la primer matriz: {tiempo_determinante_original}')
                print(f'Tiempo de proceso total: {tiempo_total}')
                print()
                opc = str(input('\n1.- Mas info\n2.- Menu\nElige una opcion: '))
                if opc == '1':
                    mostrar = masinfo(datos, determinante_original, matrices, determinantes)
                elif opc == '2':
                    mostrar = False
                else:
                    print('Opcion no valida intenta nuevamente')
                    pause()
        else: 
            print(f'La determinande de la matriz')
            imprimir_matriz(datos)
            print('Es 0, no se puede resolver por este metodo')
    else:
        print('Las filas y las columnas son de tamaños diferentes')
        print(f'Filas: {filas}')
        print(f'Columnas: {columnas}')

def masinfo(datos, determinante_original, matrices, determinantes):
    clean()
    print('La determinante de la matriz: ')
    imprimir_matriz(datos)
    print(f'Es: {determinante_original}')
    print()
    for i in range(len(datos)):
        print('La determinante de la matriz: ')
        imprimir_matriz(matrices[i])
        print(f'Es: {determinantes[i]}')
        print()
    
    mostrar = True
    while mostrar:
        opc = str(input('\n1.- Regresar\n2.- Menu\nElige una opcion: '))
        if opc == '1':
            return True
        elif opc == '2':
            return False
        else:
            print('Opcion no valida intenta nuevamente')
            pause()


def main():
    global encontradas
    global no_encontradas
    global determinantes_no_encontradas
    clean()
    n = int(input('Ingresa el tamaño de la matriz: '))
    #n = 3
    veces = int(input('Ingresa el numero de veces a realizar: '))
    #veces = 50000
    comparaciones = int(input('Numero de comparaciones: '))
    #comparaciones = 100
    #clean()
    datos_promedio = []
    for bucle in range(comparaciones):
        encontradas = 0
        no_encontradas = 0
        inicio = time.time()
        for vez in range(veces):
            datos = []
            #resultados = []
            for i in range(n):
                datos.append([])
                donde.append(0)
                for _ in range(n):
                    datos[i].append(random.randrange(-10, 11))
                    #datos[i].append(random.randrange(0, 2))
            """ for i in range(n):
                resultados.append([])
                resultados[i].append(random.randrange(5 * n, 100 * n))
            solucion(datos, resultados) """
            det = determinante_base(datos)
        fin = time.time()
        total = fin - inicio
        #imprimir_matriz(datos)
        print(f'{bucle + 1}.- Tiempo total en tomar {veces} determinantes de {n}x{n}: {total}')
        print(f'Encontradas: {encontradas} --- No encontradas: {no_encontradas}')
        print(f'Total: {encontradas + no_encontradas}\t\t{bucle + 1} de {comparaciones}')
        print('--------------------------\n')

        datos_promedio.append(total)
    promedio = sum(datos_promedio) / len(datos_promedio)
    print(f'El promedio de tiempo fue {promedio} --- Tiempo total: {sum(datos_promedio)}')
    print(f'Salvadas de repetir en diccionario: {iguales} --- Encontradas en db: {encontradas_en_db}')
    print()
    print('Actualizando datos...')

    nombre = '['
    for _ in range(n - 1):
        nombre += '['
    for i in range(len(donde)):
        if donde[i] > 0:
            print(f'Agregando a la matriz {i + 2}x{i + 2}: {donde[i]}')
    determinantes_no_encontradas[f'{nombre}'] = 0
    agregar(determinantes_no_encontradas)
    determinantes_no_encontradas = {}
    #clean()


if __name__ == '__main__':
    main()
    conexion.close()
