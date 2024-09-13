if __name__ == '__main__':
    records = []
    for idx in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    objetos_ordenados = sorted(records, key=lambda x: x[1], reverse=True)
    size = len(objetos_ordenados)
    seleccionados = []
    #Calcular el second lowest grade
    iterador = 2
    while True:
        if(objetos_ordenados[size-iterador][1] == objetos_ordenados[size-1][1]):
            iterador += 1
        else:
            break
        
    for item in objetos_ordenados:
        if(item[1] == objetos_ordenados[size-iterador][1]):
            seleccionados.append(item)
    objetos_ordenados2 = sorted(seleccionados, key=lambda x: x[0])
    for lastArr in objetos_ordenados2:
        print(lastArr[0])

    
