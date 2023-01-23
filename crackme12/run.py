
k=1
key =['%',1,2,'k',4,5,'^',7,8,'f',10,11,'F',13]
    
#key[3] = 'k'
#key[12] = 'F'
#key[0] = '%'
#key[9] = 'f'
#key[6] = '^'


for i in range(255):
    if i << 2 == 0xc4:
        key[11]=chr(i)
    if i << 2 == 0xe4:
        key[5]=chr(i)
    if i << k == 0xf6:
        key[7] = chr(i)
    if i << k == 0xc8:
        key[1] = chr(i)
    if i << k == 0x68:
        key[13] = chr(i)
    if i << 2 == 0xb8:
        key[8] = chr(i)
    if i << k == 0xd4:
        key[2] = chr(i)
    if i << k == 0x80:
        key[10] = chr(i)
    if i << k == 0x50:
        key[4] = chr(i)
    
print(''.join(key))
quit()
