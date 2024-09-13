import numpy

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(numpy.reshape(arr,(3,3)))