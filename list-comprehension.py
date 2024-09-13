if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    permutaciones = []
    
    for l in range(x+1):
        list_temp = []
        for j in range(y+1):
                for i in range(z+1):
                    suma = l + j + i
                    if suma != n:
                        permutaciones.append([l,j,i])
    print(permutaciones)
               
               
   
         
         


    
    