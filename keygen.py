#this program will take the number of solutions to be printed , the solutions are printed in ascending order
#example : python keygen.py 10
#will print the first 10 solutions
from math import sqrt

import sys

number_keys = int(sys.argv[1])

def isitprime(n):
 prime_flag = 0   
 if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        return 1
    else:
        return 0
 else:
    return 0
    
    
c = 1
while number_keys >= 0:

    
        if (len(str(c))%3 == 0) and isitprime(c) :
            print (c)
            number_keys-=1
        c+=1        
