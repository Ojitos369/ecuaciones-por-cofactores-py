try:
    from src.extras import clean, convert_float, pause
except:
    from extras import clean, convert_float, pause
import time
import random
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
    longitud = len(mat)
    if longitud == 2:
        a = mat[0][0] * mat[1][1]
        b = mat[1][0] * mat[0][1]
        return a - b
    else:
        determinante = 0
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
            imprimir_matriz(mat)
            resultados_cofactores.append(c)
        for i in range(len(resultados_cofactores)):
            if i % 2 == 0:
                determinante += resultados_cofactores[i]
            else:
                determinante -= resultados_cofactores[i]
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
    clean()
    n = int(input('Ingresa el tamaño de la matriz: '))
    datos = []
    resultados = []
    for i in range(n):
        datos.append([])
        for _ in range(n):
            datos[i].append(random.randrange(15))
    for i in range(n):
        resultados.append([])
        resultados[i].append(random.randrange(5 * n, 100 * n))
    solucion(datos, resultados)

if __name__ == '__main__':
    main()