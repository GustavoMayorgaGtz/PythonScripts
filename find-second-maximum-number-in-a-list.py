if __name__ == '__main__':
    n = int(input())  # Número de elementos en la lista
    arr = list(map(int, input().split()))  # Convertir la entrada a una lista de enteros
    arr.sort()  # Ordenar la lista en orden ascendente
    s = len(arr)  # Longitud de la lista ordenada
    max = arr[s-1]
    iterador = 1
    
    while True:
        if max == arr[s-iterador]:
            iterador += 1
        else:
            print(arr[s-iterador])
            break