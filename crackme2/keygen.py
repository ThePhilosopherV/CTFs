import random
import string

edx=0xffff

chars = string.ascii_letters + string.digits + string.punctuation

while True:
    
    k=0
    dl=3
    ns=""
    h=0
    n=0
    
    key = ''.join(random.choice(chars) for i in range(13))

    for c in key:
        ns+=chr(ord(c) ^ dl ^ 0x4d)
        
        dl+=1

    while 1:
        
        c=ns[k]
        n+=ord(c)  * h
        
        h+=edx
        
        k+=1
        
        if (h == 0x0CFFF3):
            
            break

    if (n == 0x931F6CE):
        print(key)
        break
        





















