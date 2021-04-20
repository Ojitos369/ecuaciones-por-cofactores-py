from src.extras import clean, convert_float, pause
import src.operaciones_complejas as operaciones
def imprimir_matriz(mat):
    try:
        filas = len(mat)
        columnas = len(mat[0])
    except:
        filas = 0
        columnas = 0
    for i in range(filas):
        for j in range(columnas):
            cero = False
            try:
                if mat[i][j][0]:
                    print(f'{mat[i][j][0]}', end='')
                else:
                    print(f'{mat[i][j][0]}', end='')
                    cero = True
                if mat[i][j][1] != 0:
                    if mat[i][j][1] > 0:
                        print(f'+{mat[i][j][1]}i', end='')
                    else:
                        print(f'{mat[i][j][1]}i', end='')
                else:
                    cero = True
                if cero:
                    print('',end='\t\t')
                else:
                    print('',end='\t')
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
            ma[i].append([])
            imprimir_matriz(ma)
            numero = input(f'\nIngresa la parte REAL de la posicion {i+1},{j+1}: ')
            numero = convert_float(numero)
            if numero:
                ma[i][j].append(numero)
            else:
                ma[i][j].append(0)
            clean()
            print(f'{text}')
            imprimir_matriz(ma)
            numero = input(f'\nIngresa la parte IMAGINARIA de la posicion {i+1},{j+1}: ')
            numero = convert_float(numero)
            if numero:
                ma[i][j].append(numero)
            else:
                ma[i][j].append(0)
    clean()
    print('Matriz: ')
    imprimir_matriz(ma)
    pause()
    return ma

def det3x3(mat):
    a = operaciones.producto(mat[1][1], mat[2][2])
    b = operaciones.producto(mat[1][1], mat[2][2])
    primero = operaciones.producto(mat[0][0], operaciones.resta(a, b))

    a = operaciones.producto(mat[0][1], mat[2][2])
    b = operaciones.producto(mat[0][2], mat[2][1])
    segundo = operaciones.producto(mat[1][0], operaciones.resta(a, b))

    a = operaciones.producto(mat[0][1], mat[1][2])
    b = operaciones.producto(mat[0][2], mat[1][1])
    tercero = operaciones.producto(mat[2][0], operaciones.resta(a, b))

    determinante = operaciones.suma(primero, operaciones.resta(tercero, segundo))
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
    primero = operaciones.producto(mat[0][0], det3x3(aux3))

    auxi=0
    for i in range(3):
        if i==1: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    segundo = operaciones.producto(mat[1][0], det3x3(aux3))

    auxi=0
    for i in range(3):
        if i==2: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    tercero = operaciones.producto(mat[2][0], det3x3(aux3))

    auxi=0;
    for i in range(3):
        if i==3: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    cuarto = operaciones.producto(mat[3][0], det3x3(aux3))

    negativos = operaciones.suma(segundo, cuarto)
    positivos = operaciones.suma(primero, tercero)

    determinante = operaciones.resta(positivos, negativos)
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
    longitud = len(datos)
    if determinante_original[0] != 0 and determinante_original[1] != 0:
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
                resultado = operaciones.division(determinantes[i], determinante_original)
                real = resultado[0] / resultado[2]
                real = round(real, 5)
                imaginaria = resultado[1] / resultado[2]
                imaginaria = round(imaginaria, 5)

                if resultado[1] > 0 and resultado[2] > 0: 
                    print(f'El valor {i+1} es: ({resultado[0]}+{resultado[1]}i)/{resultado[2]} = {real}+{imaginaria}i')
                elif resultado[1] < 0 and resultado[2] > 0:
                    print(f'El valor {i+1} es: ({resultado[0]}{resultado[1]}i)/{resultado[2]} = {real}-{-1*imaginaria}i')
                elif resultado[1] < 0 and resultado[2] < 0: 
                    print(f'El valor {i+1} es: ({resultado[0]}+{resultado[1]}i)/{resultado[2]} = {real}+{imaginaria}i')
                elif resultado[1] > 0 and resultado[2] < 0:
                    print(f'El valor {i+1} es: ({resultado[0]}{resultado[1]}i)/{resultado[2]} = {real}-{-1*imaginaria}i')
                else:
                    print(f'El valor {i+1} es: ({resultado[0]}/{resultado[2]} = ({real})')
            opc = str(input('\n1.- Mas info\n2.- Menu\nElige una opcion: '))
            if opc == '1':
                mostrar = masinfo(datos, determinante_original, matrices, determinantes)
            elif opc == '2':
                mostrar = False
            else:
                print('Opcion no valida intenta nuevamente')
                pause()
    else:
        print('La determinande de la matriz: ')
        imprimir_matriz(datos)
        print('Es 0, no tiene solucion por este metodo')

def masinfo(datos, determinante_original, matrices, determinantes):
    clean()
    print('La determinante de la matriz: ')
    imprimir_matriz(datos)
    if determinante_original[1] < 0:
        print(f'Es: {determinante_original[0]} - {-1 * determinante_original[1]}i')
    elif determinante_original[1] > 0:
        print(f'Es: {determinante_original[0]} + {determinante_original[1]}i')
    else:
        print(f'Es: {determinante_original[0]}')
    print()
    for i in range(len(datos)):
        print('La determinante de la matriz: ')
        imprimir_matriz(matrices[i])
        if determinantes[i][1] < 0:
            print(f'Es: {determinantes[i][0]} - {-1 * determinantes[i][1]}i')
        elif determinantes[i][1] > 0:
            print(f'Es: {determinantes[i][0]} + {determinantes[i][1]}i')
        else:
            print(f'Es: {determinantes[i][0]}')
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