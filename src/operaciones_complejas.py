def suma(com1, com2):
    res = []
    res.append(com1[0] + com2[0])
    res.append(com1[1] + com2[1])
    return res

def resta(com1, com2):
    res = []
    res.append(com1[0] - com2[0])
    res.append(com1[1] - com2[1])
    return res

def producto(com1, com2):
    res = []
    a = com1[0]*com2[0]
    b = com1[1]*com2[1]
    res.append(a - b)

    a = com1[0]*com2[1]
    b = com1[1]*com2[0]
    res.append(a + b)
    return res

def division(com2, com1):
    res = []
    div = (com2[0] ** 2) + (com2[1] ** 2)
    a = com1[0]*com2[0]
    b = com1[1]*com2[1]
    c = a + b
    res.append(c)

    a = com1[0]*com2[1]
    b = com1[1]*com2[0]
    c = -a + b
    res.append(c)

    res.append(div)
    return res

if __name__ == '__main__':
    from extras import clean
    clean()
    a = int(input('Real 1: '))
    b = int(input('Imaginario 1: '))
    c = int(input('Real 2: '))
    d = int(input('Imaginario 2: '))
    com1 = [a, b]
    com2 = [c, d]
    clean()
    print(f'Mat1: {com1}')
    print(f'Mat2: {com2}')
    print()
    print('-----------------')
    print()
    print(f'suma {suma(com1, com2)}')
    print(f'resta {resta(com1, com2)}')
    print(f'producto {producto(com1, com2)}')
    print(f'division {division(com1, com2)}')
    print()
