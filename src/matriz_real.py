from src.extras import clean, convert_float, pause
import json
import time
import random


encontradas = 0
no_encontradas = 0
"""try:
    print('Iniciando...')
    with open('determinantes.json', 'r') as f:
        diccionario_de_determinantes = json.load(f)
    clean()
except:
    diccionario_de_determinantes = {}
"""
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
    #global diccionario_de_determinantes
    global encontradas
    global no_encontradas
    longitud = len(mat)
    if longitud == 1:
        return mat[0][0]
    else:
        determinante = 0
        try:
            #print('Iniciando...')
            with open(f'determinantes_{longitud}x{longitud}.json', 'r') as f:
                diccionario_de_determinantes = json.load(f)
            #clean()
        except:
            diccionario_de_determinantes = {}
        try:
            det = diccionario_de_determinantes[str(mat)]
            encontradas += 1
            #clean()
            """ if longitud > 2 and False:
                imprimir_matriz(mat)
                print('ENTRO Y TOMO DETERMINANTE :D ')
                print(f'{mat} : {det}')
                print() """
            #pause()
            return det
        except:
            #clean()
            #imprimir_matriz(mat)
            #print('no entro: ')
            #print(f'{mat}')
            #print()
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
            diccionario_de_determinantes[str(mat)] = determinante
            with open(f'determinantes_{longitud}x{longitud}.json', 'w') as f:
                json.dump(diccionario_de_determinantes, f, indent = 4, sort_keys=True)
            
            no_encontradas += 1
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
            mostrar = False
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
    clean()
    n = int(input('Ingresa el tamaño de la matriz: '))
    veces = int(input('Ingresa el numero de veces a realizar: '))
    comparaciones = int(input('Numero de comparaciones: '))
    #veces = 100000
    clean()
    for bucle in range(comparaciones):
        encontradas = 0
        no_encontradas = 0
        inicio = time.time()
        for vez in range(veces):
            datos = []
            #resultados = []
            for i in range(n):
                datos.append([])
                for _ in range(n):
                    datos[i].append(random.randrange(-10, 11))
            """ for i in range(n):
                resultados.append([])
                resultados[i].append(random.randrange(5 * n, 100 * n))
            solucion(datos, resultados) """
            determinante_base(datos)
        fin = time.time()
        total = fin - inicio
        #imprimir_matriz(datos)
        print(f'{bucle + 1}.- Tiempo total en tomar {veces} determinantes de {n}x{n}: {total}')
        print(f'Encontradas: {encontradas} --- No encontradas: {no_encontradas}')
        print(f'Total: {encontradas + no_encontradas}')
        print('--------------------------\n')
        """with open('determinantes.json', 'w') as f:
                json.dump(diccionario_de_determinantes, f, indent = 4, sort_keys=True)"""
    print('Cerrando...')
    
    
    #clean()

if __name__ == '__main__':
    main()
