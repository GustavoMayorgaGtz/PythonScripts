#Given an integer, n, perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    residuo = n % 2
    #Es par
    if residuo == 0: 
         if n >= 2 and n <= 5:
            print('Not Weird')
         if n >= 6 and n <= 20:
            print('Weird')
         if n > 20:
            print('Not Weird')
        
    else: 
    #Es impar 
         print('Weird')
                   