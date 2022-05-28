#the following program does three things:
#First : getting the first 624 random values by Xoring 'flag.jpg.enc' with 'flag.jpg.partial'
#Second : generating the next random values and stores them in a file 
#Third : Xor the random values stored previously in a file with the 'flag.jpg.enc' file to get the flag.jpg file
import random
from mt19937predictor import MT19937Predictor #importing the Mersenne Twister predictor class  
from binascii import hexlify

predictor = MT19937Predictor() 
s=''

k=0

with open('flag.jpg.enc', 'r') as f1, open('flag.jpg.partial', 'r') as f2:
#openning 'flag.jpg.enc' and 'flag.jpg.partial' in read mode

    while 1:
        
        c1 = f1.read(4) # reading 4 characters ,each loop cycle we get the next 4 characters
        c2 = f2.read(4)
     
        if k == 625:#k>624 this means we have enough values to predict next values
            while 1:
                if k == 15200:# k should be at least 15106 (15106 is the length of the flag.jpg.enc divided by four) 
                               # just to make sure we have enough random numbers for decryption  
                    with open('flag.jpg.enc','r') as f1 , open('stream.txt','r') as f2:
                        lst = f2.read().splitlines()#stores our random values in list
                        k=0
                        s=''
                        while 1:
                            if k == 15105:
                                  open('flag.jpg','w').write(s)#Write the decrypted string to flag.jpg file
                                  quit()
                            c1 = f1.read(4)
                            c2 = hex(int(lst[k]))[2:].replace('L', '').zfill(8).decode("hex")#Convert decimal random value to ascci characters
        
                            for i in range(4):
                                #here we Xor each four characters of flag.jpg.enc 
                                #with the coresponding random four characters  
                                s+=chr(ord(c1[i])^ord(c2[i])) 
                            k+=1
                    
                open('stream.txt','a').write(str(predictor.getrandbits(32))+'\n')#we store the predicted future values in stream.txt file
                
                k+=1     

        
        for i in range(4):
            s+=chr(ord(c1[i])^ord(c2[i]))#Xor flag.jpg.enc character with flag.jpg.partial to get the initial random values
        
        b=int(hexlify(s),16)#convert hex to decimal
        
        open('stream.txt','a').write(str(b)+'\n')# we store the first 624 random values
        
        predictor.setrandbits(b,32) # setting up the first 624 input for the PRNG predictor   
            
        k+=1
        s=''

