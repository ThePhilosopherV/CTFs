
data = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?'


key = '2085442295234491944718512044618151344208544201516'
       

# "the*view*is*great*from*the*top"
c=0
while 1:
    if c >= len(key):
        quit()
    if   c == 23:
        print(data[int(key[c])-1],end='')
        c+=1
    try:
        print(data[int(key[c:c+2])-1],end='')
        c+=2
    except:
        
        print(data[int(key[c])-1],end='')
        c+=1
        
    
    


