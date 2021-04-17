from src.extras import clean, convert_float, pause
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
                #print(mat)

def ingresar_matriz(filas, columnas, text=''):
    ma=[]
    for i in range(filas):
        ma.append([])
        for j in range(columnas):
            clean()
            print(f'{text}')
            imprimir_matriz(ma)
            inc = True
            while inc:
                numero = input(f'\nIngresa el numero de la posicion {i+1},{j+1}: ')
                numero = convert_float(numero)
                if numero:
                    ma[i].append(numero)
                    inc = False
                else:
                    ma[i].append(0)
                    inc = False
    clean()
    print('Matriz: ')
    imprimir_matriz(ma)
    pause()
    return ma

def det3x3(mat):
    primero = mat[0][0]*((mat[1][1]*mat[2][2])-(mat[1][2]*mat[2][1]))
    segundo = mat[1][0]*((mat[0][1]*mat[2][2])-(mat[0][2]*mat[2][1]))
    tercero = mat[2][0]*((mat[0][1]*mat[1][2])-(mat[0][2]*mat[1][1]))
    determinante = primero-segundo+tercero
    return determinante

def det4x4(mat):
    aux3=[]
    for i in range(3):
        aux3.append([1,1,1])

    auxi=0
    for i in range(3):
        if i==0: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    primero = mat[0][0] * det3x3(aux3)

    auxi=0
    for i in range(3):
        if i==1: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    segundo = mat[1][0] * det3x3(aux3)

    auxi=0
    for i in range(3):
        if i==2: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    tercero = mat[2][0] * det3x3(aux3)

    auxi=0;
    for i in range(3):
        if i==3: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    cuarto = mat[3][0] * det3x3(aux3)

    determinante = primero-segundo+tercero-cuarto;
    return determinante;

def determinante(mat):
    filas = len(mat)
    columnas = len(mat[0])
    if filas == columnas:
        if filas == 3:
            return det3x3(mat)
        elif filas == 4:
            return det4x4(mat)
        else:
            print('Tranajando matrices mas grandes')
            return False
    else:
        print('Las filas y las columnas son de tamaños diferentes')
        print(f'Filas: {filas}')
        print(f'Columnas: {columnas}')
    pause()

def solucion(datos, resultados):
    clean()
    determinantes = []
    determinante_original = determinante(datos)
    longitud = len(datos)
    print('Datos')
    imprimir_matriz(datos)
    print('Resultados')
    imprimir_matriz(resultados)
    for i in range(longitud):
        matriz_auxiliar = []

        for elemento in datos:
            matriz_auxiliar.append(elemento[:])

        for j in range(longitud):
            matriz_auxiliar[j][i] = resultados[j][0]

        determinantes.append(determinante(matriz_auxiliar))
    for i in range(len(determinantes)):
        print(f'El valor {i+1} es: {determinantes[i]/determinante_original}')