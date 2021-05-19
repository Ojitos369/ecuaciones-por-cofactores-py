# ------------- Imports --------
from src.extras import clean, pause
import src.menus as menus
from time import sleep
import src.matriz_real as matrices
import src.matriz_compleja as complejas


# ------------- Functions --------

def main():
    show_menu = True
    while show_menu:
        #opc = menus.main()
        opc = 1
        if opc == 1:
            reales = 369
            reales = menus.size()
            if reales == 1:
                datos = matrices.ingresar_matriz(3,3,'Ingresa los datos de la matriz de datos: ')
                resultados = matrices.ingresar_matriz(3,1,'Ingresa los resultados: ')
                matrices.solucion(datos, resultados)
            elif reales == 2:
                datos = matrices.ingresar_matriz(4,4,'Ingresa los datos de la matriz de datos: ')
                resultados = matrices.ingresar_matriz(4,1,'Ingresa los resultados: ')
                matrices.solucion(datos, resultados)
            elif reales == 3:
                n = menus.numero()
                datos = matrices.ingresar_matriz(n,n,'Ingresa los datos de la matriz de datos: ')
                resultados = matrices.ingresar_matriz(n,1,'Ingresa los resultados: ')
                matrices.solucion(datos, resultados)
            elif reales == 369:
                matrices.main()
                #show_menu = False
            elif reales == 365:
                clean()
                matrices.aleatoria()
            else:
                opc = 3
                show_menu = False

        elif opc == 2:
            clean()
            print('Arreglando errores, no disponible de momento. Lamentamos las molestias')
            pause()
            """ imaginarios = menus.size()
            if imaginarios == 1:
                datos = complejas.ingresar_matriz(3,3,'Ingresa los datos de la matriz de datos: ')
                resultados = complejas.ingresar_matriz(3,1,'Ingresa los resultados: ')
            elif reales == 2:
                datos = complejas.ingresar_matriz(4,4,'Ingresa los datos de la matriz de datos: ')
                resultados = complejas.ingresar_matriz(4,1,'Ingresa los resultados: ') """
#            try:
            #complejas.solucion(datos, resultados)
                #pause()
#            except:
#                pass

        elif opc == 3:
            print('Adios.')
            sleep(.5)
            clean()
            show_menu = False

# ------------- Entry Point --------
if __name__ == '__main__':
    main()
