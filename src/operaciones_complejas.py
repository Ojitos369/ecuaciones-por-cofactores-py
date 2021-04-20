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