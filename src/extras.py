import os
def clean():
    try:
        os.system('clear')
    except:
        os.system('cls')

def pause():
    input('Presiona Enter para continuar')

def convert_int(num):
    try:
        num = int(num)
    except:
        if num == '0' or num == 0:
            num = 0
        else:
            num = False
    return num

def convert_float(num):
    try:
        num = float(num)
    except:
        if num == '0' or num == 0:
            num = 0
        else:
            num = False
    return num