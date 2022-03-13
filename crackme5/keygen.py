import random
import string


chars = string.ascii_letters 


username=''.join(random.choice(chars) for x in range(6))

print "username: " + username

user_encrypt=""

for c in username:
    r = ord(c)^26
    rem = r % 6
    user_encrypt+=username[rem]

print "password: "+user_encrypt

    
