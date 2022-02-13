#https://crackmes.one/crackme/6200247933c5d46c8bcbfc4c
import random
import string

chars =  string.ascii_letters.lower() #+ string.digits  + string.punctuation #  string.digits  + string.punctuation  + string.ascii_letters #+


while (1):
    key=''.join(random.choice(chars) for x in range(16))
   
    # eax =[ (byte_pointer(0xEFFD28 + 0x0c) - key[3])*(key[6]-key[3]) ] * (key[8]-key[12])*4 + (key[13]-key[15])*(key[13]-key[15])
    
    val =((ord(key[13])-ord(key[14])+2)*(ord(key[1]) - 4 - ord(key[3]) ) * (ord(key[12]) - 5 - ord(key[2]))*0x88 + (ord(key[1]) - ord(key[2])) * (ord(key[1]) - ord(key[2])))
    
    
    if val == -36992 :
        
        part1 = key[1:4]
        part2 = key [12:15]
        
        for i in range (500):
            mk=''.join(random.choice(chars) for x in range(8))
            
            one_c =''.join(random.choice(chars) for x in range(1))
           
            key=key[0]+part1+mk+part2+one_c
            #key=key.upper()
            
            
            
            #          (key [13] - key[14] + 2)*(key[1] - 4 - key[3])*(key[12] - key[2] - 5)*0x88 + (key[1] - key[2])*(key[1] - key[2])
            val2 = (ord(key[12]) - ord(key[3]))*(ord(key[6])-ord(key[3]))  * (ord(key[8])-ord(key[12]))*4 +  (ord(key[13])-ord(key[15]))*(ord(key[13])-ord(key[15]))
            
            
            if  val2 == 0x11B8:
            
                print key
                quit()
        
        

                      #68h ; h
#debug013:012FFCB9 db  65h ; e
#debug013:012FFCBA db  79h ; y
#debug013:012FFCBB db  73h ; s
#debug013:012FFCBC db  61h ; a
#debug013:012FFCBD db  6Ch ; l
#debug013:012FFCBE db    0   not changed   
#debug013:012FFCBF db    0   not changed
#debug013:012FFCC0 db 0E5h ;  not changed
#debug013:012FFCC1 db 0DCh ;  not changed
#debug013:012FFCC2 db  22h ; " not changed
#debug013:012FFCC3 db    0     not changed
#debug013:012FFCC4 db 0E4h ;  changed
#debug013:012FFCC5 db 0FCh ;  changed
#debug013:012FFCC6 db  2Fh ; / changed
#debug013:012FFCC7 db    1     changed
#debug013:012FFCC8 db    6
#debug013:012FFCC9 db    0
#debug013:012FFCCA db    0
#debug013:012FFCCB db    0
#debug013:012FFCCC db  0Fh
