
import ctypes

user=input('Username: ')
print("Password: ",end='')
for c in user:
    sum=ord(c) + 0xbf -0xd
    sum= ((sum >> (8 * 0)) & 0xff)
    if sum < 0 :
        print( chr(ord(c) + 0xd) ,end='')
        continue 
    
    sum-=0xd
    sum= ((sum >> (8 * 0)) & 0xff)
    if ctypes.c_int8(sum).value <0 :
        print( chr(ord(c) - 0xd) ,end='')
        continue

    sum+=0xfa-0xd
    sum= (sum >> (8 * 0)) & 0xff
    if ctypes.c_int8(sum).value < 0 :
        print( chr(ord(c) + 0xd) ,end='')
        continue

    sum-=0xd
    if ctypes.c_int8(sum).value < 0  :
        print( chr(ord(c) - 0xd) ,end='')
        continue