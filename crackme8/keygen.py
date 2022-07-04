import random,string

letters = string.ascii_letters

while 1:
    key =  ''.join(random.choice(letters) for i in range(11))

    r8d = ord(key[9])
    eax = ord(key[10])
    r8d = r8d - eax
    edx =  ord(key[5])
    eax =  ord(key[3])
    edx = edx - eax
    ecx =  ord(key[6])
    eax =  ord(key[0])
    ecx = ecx - eax
    edx = edx * ecx
    r8d = r8d * r8d
    eax = edx * 0x88
    r8d = r8d + eax
    if r8d == 0x660:
        print(key)
        quit()
    
