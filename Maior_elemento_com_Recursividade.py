def maior_numero(lista):
    if len(lista) == 1:
        return lista[0]
    elif lista[0] < lista[-1]:
        lista[0] = lista[-1]
        return maior_numero(lista[:-1])
    else:
        return maior_numero(lista[:-1])

print(maior_numero([12, 42, 90, 3, 50, 123, 10, 21]))