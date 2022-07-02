import random,string,time


k=0
letters = string.ascii_lowercase #  + string.punctuation + string.digits #+ string.ascii_letters  + string.digits  + string.punctuation + string.ascii_lowercase   + string.ascii_uppercase + string.digits + string.punctuation
#print(letters)
#quit()

while 1:
    key =  ''.join(random.choice(letters) for i in range(15))
    #key="rb/.WfA,*(5VrAA"
    if (ord(key[14])-ord(key[13])==0) and (ord(key[10])-ord(key[9]) > 0) and (ord(key[12])-ord(key[11])) > 0:
        #if   (ord(key[8])-ord(key[7])) * (ord(key[12])-ord(key[13])) * (ord(key[10])-ord(key[9])) == -2912:
        #if ((ord(key[14])-ord(key[13])) * (ord(key[14])-ord(key[13])))  +   ((ord(key[8])-ord(key[7])) * (ord(key[12])-ord(key[13])) * (ord(key[10])-ord(key[9])) * 4) == -2912:
            edx=  (ord(key[8]) - ord(key[7]) ) * (ord(key[12]) - ord(key[11]) )
            #print("_"*10)
##            print(hex((ord(key[8]) - ord(key[7]) )))
##            print(hex((ord(key[12]) - ord(key[11]))))
##                  
##            print(hex(edx))
            ecx= (ord(key[14])-ord(key[13])) * (ord(key[14])-ord(key[13])) *  (ord(key[14])-ord(key[13])) * (ord(key[14])-ord(key[13]))
           # print(hex(ecx))
            edx=edx*(ord(key[10])-ord(key[9]))
            #print(hex(edx))
            eax=ecx+edx*4
            #print(hex(eax))
            if eax == -2912:
                key1=key
                while 1:
                    letters = string.ascii_lowercase#  + string.digits + string.ascii_letters   
                    
                    key =  ''.join(random.choice(letters) for i in range(3))
                    key="vla"+key
                
                    eax=ord(key[0])
                    var_2c = eax
                    ebx=ord(key[1])
                    eax=ord(key[2])
                    #print("xmm1:")
                    xmm1 = eax
                    #print(hex(xmm1))
                    eax = ord(key[3])
                    #edx=0
                    
                    #eax = eax - edx
                    #eax = eax - 1
                    eax = eax >> 1
                    xmm1 = xmm1 * 0.5
##                    print("xmm1:")
##                    print(xmm1)
                    #print(eax)
                    xmm2 = eax
                    eax = ord(key[4])
                    #edx=0
                    #eax = eax - edx
##                    print("edx:")
##                    print(hex(edx))
##                    print("eax:")
##                    print(hex(eax))
                    edx = eax
                    edx = edx >> 1
                    edx = edx * edx
                    #print("edx:")
                    #print(hex(edx))
                    eax = ord(key[5])
                    #print("eax:")
                    #print(hex(eax))
                    eax = eax * ebx
                    #print("eax:")
                    #print(hex(eax))
                    eax = eax - edx
                    #print("eax:")
                    #print(eax)
                    xmm0 = eax
                   
                    #print(key)
                    #quit()
                    if xmm0 == 8388:
##                        print("phase 1")
##                        print(key[:6]+key1[6:])
                        

                        eax=ebx
                        xmm1 = xmm1*xmm1
                        eax=eax*var_2c
                        xmm0 = eax
                        xmm0 = xmm0 - xmm1

                        if xmm0 == 10391.75:
                           
                            k+=1
                           
                            
                            #input()
                            

                            xmm1 = ebx
                            xmm0 = edx
                            
                            xmm1 = xmm1 * xmm2
                            
                            xmm1 = xmm1 - xmm0
                            
##                            print("="*30)
##                            print("phase 2")
##                            print(key[:6]+key1[6:])
##                            print("xmm0 :"+ str(xmm0))
##                            print("xmm1 :"+ str(xmm1))
##                            print("xmm2 :"+ str(xmm2))
##                            print("="*30)
                            #input()
                            
                            
                           
                            #input()
                            if xmm1 == 1800:
                                print(key[:6]+key1[6:])
                                quit()
                            if k==4:
                                k=0
                                break
                            
                            
                            
                            
                            
    #prord(key)
    #prord(len(key))
