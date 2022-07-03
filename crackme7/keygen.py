import random,string

letters = string.ascii_lowercase #lower case characters gave quick results

while 1:
    key =  ''.join(random.choice(letters) for i in range(15))
    
    if (ord(key[14])-ord(key[13])==0) and (ord(key[10])-ord(key[9]) > 0) and (ord(key[12])-ord(key[11])) > 0:
       
            edx=  (ord(key[8]) - ord(key[7]) ) * (ord(key[12]) - ord(key[11]) )
            
            ecx= (ord(key[14])-ord(key[13])) * (ord(key[14])-ord(key[13])) *  (ord(key[14])-ord(key[13])) * (ord(key[14])-ord(key[13]))
           
            edx=edx*(ord(key[10])-ord(key[9]))
           
            eax=ecx+edx*4
           
            if eax == -2912:
                key1=key
                while 1:
                    letters = string.ascii_lowercase #lower case characters gave quick results
                    
                    key =  ''.join(random.choice(letters) for i in range(3))
                    key="vla"+key #after many tries i noticed that prefixing keys with the word "vla" gave super fast results
                
                    eax=ord(key[0])
                    var_2c = eax
                    ebx=ord(key[1])
                    eax=ord(key[2])
                    xmm1 = eax
                    eax = ord(key[3])
                    eax = eax >> 1
                    xmm1 = xmm1 * 0.5
                    xmm2 = eax
                    eax = ord(key[4])
                    edx = eax
                    edx = edx >> 1
                    edx = edx * edx
                    eax = ord(key[5])
                    eax = eax * ebx
                    eax = eax - edx
                    xmm0 = eax
                   
                    if xmm0 == 8388:
                        
                        eax=ebx
                        xmm1 = xmm1*xmm1
                        eax=eax*var_2c
                        xmm0 = eax
                        xmm0 = xmm0 - xmm1

                        if xmm0 == 10391.75:

                            xmm1 = ebx
                            xmm0 = edx
                            xmm1 = xmm1 * xmm2                            
                            xmm1 = xmm1 - xmm0

                            if xmm1 == 1800:
                                print(key[:6]+key1[6:])
                                quit()


