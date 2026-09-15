def ordenSeleccion(lista):
    n = len(lista)
    for manoIzq in range(n):
        ind_min_val = manoIzq
        for vista in range(manoIzq + 1, n):
            if lista[vista] < lista[ind_min_val]:
                ind_min_val = vista
      
        lista[manoIzq], lista[ind_min_val] = lista[ind_min_val], lista[manoIzq]
    return lista

def ordenBurbuja(lis):
    for i in range(1, len(lis)):
        for j in range(len(lis)-1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis

def ordenInserccion(lis):
    for i in range(1, len(lis)):
        j = i
        while j > 0 and lis[j - 1] > lis[j]:
            lis[j], lis[j - 1] = lis[j - 1], lis[j]
            j -= 1
    return lis



numeros = [2, 8, 5, 3, 9, 4, 1]
print(f"Lista original: {numeros}\n")
lista_ordenada = ordenSeleccion(numeros)
print(f"\nSeleccion: {lista_ordenada}")
numeros = [2, 8, 5, 3, 9, 4, 1]
lista_ordenada = ordenBurbuja(numeros)
print(f"\nBurbuja: {lista_ordenada}")
numeros = [2, 8, 5, 3, 9, 4, 1]
lista_ordenada = ordenInserccion(numeros)
print(f"\nInserccion: {lista_ordenada}")