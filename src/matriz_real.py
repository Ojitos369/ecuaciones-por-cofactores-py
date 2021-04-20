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
    matrices = []
    determinantes = []
    determinante_original = determinante(datos)
    if determinante_original != 0:
        longitud = len(datos)
        for i in range(longitud):
            matriz_auxiliar = []

            for elemento in datos:
                matriz_auxiliar.append(elemento[:])

            for j in range(longitud):
                matriz_auxiliar[j][i] = resultados[j][0]
            
            matrices.append(matriz_auxiliar)
            determinantes.append(determinante(matriz_auxiliar))

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
            input('Presiona Enter para continuar')