import random
import string


chars = string.ascii_letters.lower() #



while (1):
    key1=''.join(random.choice(chars) for x in range(12))
    val = (ord(key1[11])+ord(key1[6]))*ord(key1[9])+ord(key1[10])*ord(key1[7])
    if val == 0x9af2:
        while(1):
            key=''.join(random.choice(chars) for x in range(12))
            #key=key1
            esi = ord(key[0])
            xmm0 = ord(key[0])
            edi = ord(key[1])
            eax = ord(key[2])
            xmm5 = ord(key[2])
            eax = ord(key[3])
            
            eax = ord(key[3])-0
            eax = (ord(key[3])>>1)

            xmm5 = (ord(key[2])*0.5) 
            xmm4 = eax=(ord(key[3])>>1)
            eax = ord(key[4])
            edx = ord(key[4])
            edx = (ord(key[4])>>1)
            xmm3 = (ord(key[4])>>1)
            edx = (ord(key[4])>>1)*(ord(key[4])>>1)
            ecx = ord(key[5])

            eax = ord(key[5])
            eax = ord(key[5]) * ord(key[1])
            xmm1 = ord(key[5])

            eax = (ord(key[5]) * ord(key[1]))-((ord(key[4])>>1)*(ord(key[4])>>1))


            xmm2 = (ord(key[5]) * ord(key[1]))-((ord(key[4])>>1)*(ord(key[4])>>1))
            

            xmm1 =  xmm1*xmm5
            xmm2 = xmm2 * xmm0
            xmm0 = xmm3
            xmm0 = xmm0*xmm4
            xmm3 = xmm3*xmm5
            xmm1 = xmm1 - xmm0
            xmm0 = edi
            xmm1 = xmm1*xmm5
            xmm0 = xmm0*xmm4
            xmm2 = xmm2 - xmm1
            xmm3 = xmm3 - xmm0
            xmm3 = xmm3 * xmm4
            xmm2 = xmm2 + xmm3

            if xmm2 == 733898.75 :
                
                print key[0:6]+key1[6]+key1[7]+"x"+key1[9]+key1[10]+key1[11]
                
                quit()
                
            
    
