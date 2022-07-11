
code="""xmm2 = 0.5
xmm0 = 0.111
eax = ord(key[0])
xmm1 = eax
eax = ord(key[1])
xmm1 = xmm1 * xmm2  
xmm1 = xmm1 + xmm0 
var_98 = xmm1 
xmm1 = eax 
eax = ord(key[2]) 
xmm1 = xmm1 * xmm2
xmm1 = xmm1 + xmm0 
var_78 = xmm1
xmm1 = eax 
eax =  ord(key[3]) 
xmm7 = eax  
xmm1 = xmm1 * xmm2 
eax =  ord(key[4])
xmm6 = eax
xmm7 = xmm7 * xmm2   
eax =  ord(key[5])
xmm5 = eax
xmm6 = xmm6 * xmm2
eax =  ord(key[6])
xmm4 = eax
xmm5 = xmm5 * xmm2 
eax =  ord(key[7])
xmm3 = eax
eax =  ord(key[8])
xmm4 = xmm4 * xmm2 
xmm3 = xmm3 * xmm2 
xmm2 = eax 
xmm3 = xmm3 + 0.128 
xmm2 = xmm2 * 0.5 
var_88 = xmm1 
var_90 = xmm5
xmm2 = xmm2 + xmm0 
xmm0 = var_78 
xmm0 = xmm0 * xmm4
eax =  ord(key[9])
var_80 = xmm0 
xmm0 = var_98 
xmm0 = xmm0 * xmm5 
xmm5 = var_80 
xmm1 = eax
xmm5 = xmm5 + xmm0 
xmm0 = var_88 
xmm1 = xmm1 * 0.5 
xmm0 = xmm0 * xmm3 
xmm5 = xmm5 + xmm0 
xmm0 = xmm7
xmm0 = xmm0 * xmm2 
xmm7 = xmm7 * xmm7
xmm5 = xmm5 + xmm0  
xmm0 = xmm6
xmm0 = xmm0 * xmm1
xmm7 = xmm7 * xmm2
xmm6 = xmm6 * xmm6 
xmm5 = xmm5 + xmm0 
xmm0 = var_78 
xmm0 = xmm0 * xmm0
xmm6 = xmm6 * xmm1 
xmm0 = xmm0 * xmm4 
var_78 = xmm0 
xmm0 = var_98
xmm4 = var_78
xmm0 = xmm0 * xmm0 
xmm0 = xmm0 * var_90 
xmm4 = xmm4 + xmm0 
xmm0 = var_88
xmm0 = xmm0 * xmm0
xmm0 = xmm0 * xmm3 
xmm4 = xmm4 + xmm0 
xmm0 = xmm5 
xmm4 = xmm4 + xmm7 
xmm4 = xmm4 + xmm6"""
##nl = []
##lst = code.splitlines()
##for l in lst:
##    r=l.split("=")
##    g=r[1].strip().split(" ")
##    if len(g)==3:
##        print(r[0]+"=f'({"+g[0]+"}" + g[1]+"{"+g[2]+"})'")
##    else:
##         print(r[0]+"=f'({"+g[0]+"})'")
    
     
    #input()

xmm2 =f'({0.5})'
xmm0 =f'({0.111})'
eax ='(ord(key[0]))'
xmm1 =f'({eax})'
eax ='(ord(key[1]))'
xmm1 =f'({xmm1}*{xmm2})'
xmm1 =f'({xmm1}+{xmm0})'
var_98 =f'({xmm1})'
xmm1 =f'({eax})'
eax ='(ord(key[2]))'
xmm1 =f'({xmm1}*{xmm2})'
xmm1 =f'({xmm1}+{xmm0})'
var_78 =f'({xmm1})'
xmm1 =f'({eax})'
eax ='(ord(key[3]))'
xmm7 =f'({eax})'
xmm1 =f'({xmm1}*{xmm2})'
eax ='(ord(key[4]))'
xmm6 =f'({eax})'
xmm7 =f'({xmm7}*{xmm2})'
eax ='(ord(key[5]))'
xmm5 =f'({eax})'
xmm6 =f'({xmm6}*{xmm2})'
eax ='(ord(key[6]))'
xmm4 =f'({eax})'
xmm5 =f'({xmm5}*{xmm2})'
eax ='(ord(key[7]))'
xmm3 =f'({eax})'
eax ='(ord(key[8]))'
xmm4 =f'({xmm4}*{xmm2})'
xmm3 =f'({xmm3}*{xmm2})'
xmm2 =f'({eax})'
xmm3 =f'({xmm3}+{0.128})'
xmm2 =f'({xmm2}*{0.5})'
var_88 =f'({xmm1})'
var_90 =f'({xmm5})'
xmm2 =f'({xmm2}+{xmm0})'
xmm0 =f'({var_78})'
xmm0 =f'({xmm0}*{xmm4})'
eax ='(ord(key[9]))'
var_80 =f'({xmm0})'
xmm0 =f'({var_98})'
xmm0 =f'({xmm0}*{xmm5})'
xmm5 =f'({var_80})'
xmm1 =f'({eax})'
xmm5 =f'({xmm5}+{xmm0})'
xmm0 =f'({var_88})'
xmm1 =f'({xmm1}*{0.5})'
xmm0 =f'({xmm0}*{xmm3})'
xmm5 =f'({xmm5}+{xmm0})'
xmm0 =f'({xmm7})'
xmm0 =f'({xmm0}*{xmm2})'
xmm7 =f'({xmm7}*{xmm7})'
xmm5 =f'({xmm5}+{xmm0})'
xmm0 =f'({xmm6})'
xmm0 =f'({xmm0}*{xmm1})'
xmm7 =f'({xmm7}*{xmm2})'
xmm6 =f'({xmm6}*{xmm6})'
xmm5 =f'({xmm5}+{xmm0})'
xmm0 =f'({var_78})'
xmm0 =f'({xmm0}*{xmm0})'
xmm6 =f'({xmm6}*{xmm1})'
xmm0 =f'({xmm0}*{xmm4})'
var_78 =f'({xmm0})'
xmm0 =f'({var_98})'
xmm4 =f'({var_78})'
xmm0 =f'({xmm0}*{xmm0})'
xmm0 =f'({xmm0}*{var_90})'
xmm4 =f'({xmm4}+{xmm0})'
xmm0 =f'({var_88})'
xmm0 =f'({xmm0}*{xmm0})'
xmm0 =f'({xmm0}*{xmm3})'
xmm4 =f'({xmm4}+{xmm0})'
xmm0 =f'({xmm5})'
xmm4 =f'({xmm4}+{xmm7})'
xmm4 =f'({xmm4}+{xmm6})'

def pxmm():
    print("xmm0="+str(xmm0))
    print("xmm1="+str(xmm1))
    print("xmm2="+str(xmm2))
    print("xmm3="+str(xmm3))
    print("xmm4="+str(xmm4))
    print("xmm5="+str(xmm5))
    print("xmm6="+str(xmm6))
    print("xmm7="+str(xmm7))
pxmm()
xmm0="((((((((((((((ord(key[1])))*(0.5))+(0.111))))*(((ord(key[6])))*(0.5)))))+(((((((ord(key[0])))*(0.5))+(0.111))))*(((ord(key[5])))*(0.5))))+((((((ord(key[2])))*(0.5))))*((((ord(key[7])))*(0.5))+0.128)))+(((((ord(key[3])))*(0.5)))*((((ord(key[8])))*0.5)+(0.111))))+(((((ord(key[4])))*(0.5)))*(((ord(key[9])))*0.5))))"
xmm1="(((ord(key[9])))*0.5)"
xmm2="((((ord(key[8])))*0.5)+(0.111))"
xmm3="((((ord(key[7])))*(0.5))+0.128)"
xmm4="((((((((((((((ord(key[1])))*(0.5))+(0.111))))*((((((ord(key[1])))*(0.5))+(0.111)))))*(((ord(key[6])))*(0.5)))))+((((((((ord(key[0])))*(0.5))+(0.111))))*((((((ord(key[0])))*(0.5))+(0.111)))))*((((ord(key[5])))*(0.5)))))+(((((((ord(key[2])))*(0.5))))*(((((ord(key[2])))*(0.5)))))*((((ord(key[7])))*(0.5))+0.128)))+(((((ord(key[3])))*(0.5))*(((ord(key[3])))*(0.5)))*((((ord(key[8])))*0.5)+(0.111))))+(((((ord(key[4])))*(0.5))*(((ord(key[4])))*(0.5)))*(((ord(key[9])))*0.5)))"
xmm5="(((((((((((((ord(key[1])))*(0.5))+(0.111))))*(((ord(key[6])))*(0.5)))))+(((((((ord(key[0])))*(0.5))+(0.111))))*(((ord(key[5])))*(0.5))))+((((((ord(key[2])))*(0.5))))*((((ord(key[7])))*(0.5))+0.128)))+(((((ord(key[3])))*(0.5)))*((((ord(key[8])))*0.5)+(0.111))))+(((((ord(key[4])))*(0.5)))*(((ord(key[9])))*0.5)))"
xmm6="(((((ord(key[4])))*(0.5))*(((ord(key[4])))*(0.5)))*(((ord(key[9])))*0.5))"
xmm7="(((((ord(key[3])))*(0.5))*(((ord(key[3])))*(0.5)))*((((ord(key[8])))*0.5)+(0.111)))"
l=[xmm0,xmm1,xmm2,xmm3,xmm4,xmm5,xmm6,xmm7]
matches=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]']
k=-1
for xmm in l:
    k+=1
    print("xmm"+str(k)+":")
    for m in matches:
        print(m+":"+str(xmm.count(m)))
##xmm0:
##[0]:1
##[1]:1
##[2]:1
##[3]:1
##[4]:1
##[5]:1
##[6]:1
##[7]:1
##[8]:1
##[9]:1
##xmm1:
##[0]:0
##[1]:0
##[2]:0
##[3]:0
##[4]:0
##[5]:0
##[6]:0
##[7]:0
##[8]:0
##[9]:1
##xmm2:
##[0]:0
##[1]:0
##[2]:0
##[3]:0
##[4]:0
##[5]:0
##[6]:0
##[7]:0
##[8]:1
##[9]:0
##xmm3:
##[0]:0
##[1]:0
##[2]:0
##[3]:0
##[4]:0
##[5]:0
##[6]:0
##[7]:1
##[8]:0
##[9]:0
##xmm4:
##[0]:2
##[1]:2
##[2]:2
##[3]:2
##[4]:2
##[5]:1
##[6]:1
##[7]:1
##[8]:1
##[9]:1
##xmm5:
##[0]:1
##[1]:1
##[2]:1
##[3]:1
##[4]:1
##[5]:1
##[6]:1
##[7]:1
##[8]:1
##[9]:1
##xmm6:
##[0]:0
##[1]:0
##[2]:0
##[3]:0
##[4]:2
##[5]:0
##[6]:0
##[7]:0
##[8]:0
##[9]:1
##xmm7:
##[0]:0
##[1]:0
##[2]:0
##[3]:2
##[4]:0
##[5]:0
##[6]:0
##[7]:0
##[8]:1
##[9]:0






##c=-1
##for e in nl:
##c+=1
##if 'xm' in e[0]:
##print(e[0]+"="+e[1])
#if 'x' in e[1]:





##if r[1].isdigit():
##nl.append(r)
##else:
##if 




#print(lst)

   



























































































