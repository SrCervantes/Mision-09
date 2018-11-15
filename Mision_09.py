# Autor: Luis Ricardo Chagala Cervnates.
# Listas nuevamente.


def extraerPares(lista):
    listaPares = []
    for k in range(len(lista)):
        if lista[k] % 2 == 0:
            listaPares.append(lista[k])
    return listaPares


def extraerMayoresPrevio(lista):
    listaMayores = []
    for k in range(1,len(lista)):
        if lista[k] > lista[k-1]:
            listaMayores.append(lista[k])
    return listaMayores


def intercambiarParejas(lista):
    listaParejas = []
    if len(lista)%2==0:
        for k in range(1,len(lista),2):
            a= lista[k]
            b= lista[k-1]
            listaParejas.append(a)
            listaParejas.append(b)
    else:
        for k in range(1,len(lista)-1,2):
            a=lista[k]
            b=lista[k-1]
            listaParejas.append(a)
            listaParejas.append(b)
        listaParejas.append(lista[-1])
    return listaParejas


def intercambiarMM(lista):
    if len(lista) > 0:
        mayor = lista[0]
        posMayor = 0
        menor = lista[0]
        posMenor = 0
        for k in range(len(lista)):
            if lista[k] < menor:
                menor = lista[k]
                posMenor = k
            elif lista[k] > mayor:
                mayor = lista[k]
                posMayor = k
        lista[posMayor] = menor
        lista[posMenor] = mayor
    return lista


def promediarCentro(lista):
    if len(lista) > 2:
        mayor = lista[0]
        posMayor = 0
        menor = lista[0]
        posMenor = 0
        suma = 0
        for k in range(len(lista)):
            if lista[k] < menor:
                menor = lista[k]
                posMenor = k
            elif lista[k] > mayor:
                mayor = lista[k]
                posMayor = k
        for k in range(len(lista)):
            if k == posMenor or k == posMayor:
                pass
            else:
                suma += lista[k]
        promedio = suma / (len(lista)-2)
        return int(promedio)
    else:
        return 0


def calcularEstadistica(lista):
    sumaM = 0
    media = 0
    sumaD = 0
    deviacion = 0
    if len(lista) > 0:
        for k in range(len(lista)):
            sumaM += lista[k]
        media = sumaM / len(lista)

        for k in range(len(lista)):
            sumaD += (lista[k]-media)**2
        deviacion = (sumaD / (len(lista)-1))**0.5

    return media,deviacion


lista = [20,55,30,5,55,5]
print(promediarCentro(lista))