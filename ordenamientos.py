def ordenSeleccion(lista):
    n = len(lista)
    for manoIzq in range(n):
        ind_min_val = manoIzq
        for vista in range(manoIzq + 1, n):
            if lista[vista] < lista[ind_min_val]:
                ind_min_val = vista
      
        lista[manoIzq], lista[ind_min_val] = lista[ind_min_val], lista[manoIzq]
      
        print(f"Paso {manoIzq+1}: {lista}")
        
    return lista

numeros = [2, 8, 5, 3, 9, 4, 1]
print(f"Lista original: {numeros}\n")
lista_ordenada = ordenSeleccion(numeros)
print(f"\nLista final ordenada: {lista_ordenada}")