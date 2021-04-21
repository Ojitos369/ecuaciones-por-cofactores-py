# ------------- Imports --------
from src.extras import pause, clean, convert_int


# ------------- Functions --------
def size():
    option = None
    incorrecto = True
    while incorrecto:
        clean()
        option = input("""1.- Sistema de ecuaciones de 3 incognitas
2.- Sistema de ecuaciones de 4 incognitas
3.- Sistema de ecuaciones de n incognitas
4.- Cancelar
Elige una opcion: """)
        option = convert_int(option)
        if option > 0 and option < 5:
            incorrecto = False
        else:
            print('Opcion no valida. Intenta nuevamente')
            pause()
    return option

def numero():
    inc = True
    while inc:
        clean()
        n = input('Ingresa un numero: ')
        n = convert_int(n)
        if n > 0:
            return n
        else:
            print('Numero no valido, debe ser un numero entero positivo, intenta nuevamente.')
            pause()

def main():
    option = None
    incorrecto = True
    while incorrecto:
        clean()
        option = input("""1.- Reales
2.- Imaginarios
3.- Salir
Elige una opcion: """)
        option = convert_int(option)
        if option > 0 and option < 4:
            incorrecto = False
        else:
            print('Opcion no valida. Intenta nuevamente')
            pause()

    return option


# ------------- Entry Point --------
if __name__ == '__main__':
    main()