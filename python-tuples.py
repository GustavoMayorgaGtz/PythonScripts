if __name__ == '__main__':
   # Leer el número de elementos en la tupla
    n = int(input())  # En este caso, n sería 2

# Leer los n enteros como una lista y luego convertirla a una tupla
    t = tuple(map(int, input().split()))  # En este caso, t sería (1, 2)

# Calcular y mostrar el valor del hash de la tupla
    print(hash(t))
