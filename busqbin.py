def busqueda_binaria(array, numero):
    menor = 0
    mayor = len(array) - 1
    for data in range(len(array)):
        medio = (menor + mayor) // 2
        if array[medio] == numero:
            return medio
        elif array[medio] < numero:
            menor = medio
        else:
            mayor = medio
        if mayor - menor <= 1:
            break
    if array[menor] == numero:
        return menor
    elif array[mayor] == numero:
        return mayor
    return -1

array = [4,5,10,20,25,30,35,40,45,50,58,65,80,98]
print("Array: ", array)
numero = int(input("Ingrese un número a buscar: "))
busqueda = busqueda_binaria(array, numero)
if busqueda == -1:
    print(f"El número {numero} no se encuentra en el array.")
else:
    print(f"El número {numero} se encuentra en la posición {busqueda} del array.")