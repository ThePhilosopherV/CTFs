data=0xBD,0x35,0xA9,0xA1,0xD1,0xE1,0xD9,0x35,0x31,1,0x39,0xD9,0xAA,0x95,1,0xAA,0xFD,0xB9,0x28,0xD5,0x7C,0xD9,0x1D,0x95,0x99,0xCD,0xD9,0xF1,0xAA,0xD2,0xEE,0xF9

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

for c in data:
    for i in range(255):
        a= i ^ 0x54
        a=rol(a,2,8)
        a=a+0xeb
        a = int('0x'+hex(int(str( a )))[-2:],16)
        a=a^0x24


        a=a^0x54
        a=rol(a,2,8)
        a=a^0x24
        a=a^0x54
        
        
        a=a^0x24
        a=a^0x54
        a=rol(a,2,8)
        a=a^0x24

        a=rol(a,2,8)
        a+=0xeb
        a=a^0x24
        a=rol(a,2,8)
        if a == c:
            print(chr(i),end='') 
            

    
    
    
    
    
       
