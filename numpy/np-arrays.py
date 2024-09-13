import numpy

def arrays():
    arr = input().strip().split(' ')
    arr.reverse()
    result = numpy.array(arr, float)
    print(result)
    
    
if __name__ == '__main__':
    arrays()
    
