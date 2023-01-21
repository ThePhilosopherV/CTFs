
%include "myfunctions.asm"

section .data

o1 db " _    _      _                            _____  ",0xa    
o2 db "| |  | |    | |                          |_   _| "    ,0xa
o3 db "| |  | | ___| | ___ ___  _ __ ___   ___    | | ___ "  ,0xa
o4 db "| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \  ",0xa
o5 db "\  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) | ",0xa
o6 db " \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/  ",0xa,0xa
o7 db " _____ _           ___  ___      _        _",0xa          
o8 db "|_   _| |          |  \/  |     | |      (_)",0xa         
o9 db "  | | | |__   ___  | .  . | __ _| |_ _ __ ___  __",0xa    
o10 db "  | | | '_ \ / _ \ | |\/| |/ _` | __| '__| \ \/ /",0xa    
o11 db "  | | | | | |  __/ | |  | | (_| | |_| |  | |>  <",0xa     
o12 db "  \_/ |_| |_|\___| \_|  |_/\__,_|\__|_|  |_/_/\_\",0xa,0xa    
o13 db "Sometimes going down the rabbit hole is the only path to the truth",0xa,0                                                   

usermsg db  "Username: ",0
passmsg db  "Password: ",0

user    db  "admin",0
pass    db  "password",0

credsmsg    db  "Correct credentials",0x0A,0
badcredsmsg    db  "Wrong credentials",0x0A,0

key1msg  db  "Input a valid key: ",0

gkey   db   "Correct key",0x0A,0
bkey   db   "Wrong key",0x0A,0

gsol   db   "Congradulations, you managed to beat the Matrix!",0x0A,0

enterance  db   "_____________{The Enterance}___________",0x0A,0x0A,0
simple   db   '"Always check the door first!"',0x0A,0x0A,0
theopening  db   "_____________{The Opening}___________",0x0A,0x0A,0
myster   db   '"Decode the mysteries of nature!"',0x0A,0x0A,0
themiddlegame  db  "_____________{The Middlegame}___________",0x0A,0x0A,0
rome    db   '"All roads lead to rome!"',0x0A,0x0A,0
theendgame  db  "_____________{The Endgame}___________",0x0A,0x0A,0

base64   db   "RCdgJUBwb0o2fGtXMjd4d0FRPz49cE1ubko3WkdpZ0NDQS8/YT5PXykocnFwdXRtbDJwaWhtbGtqaWhnYCZHXWJhWll9QD9bVFN3UVB0VE1McEpPSGxMLkpJSEdAZEQmQkE6OThcfTU6MzgxVS8uMyxQcSkuJyYlJEgoJyYlJGQieT99X3U7eXh3dm81bXJxamluZ2YsZGNoZ2ZlXl0jW2BZWF1WenlTUlFQVU5yTFFKbk4wL0VEQ2dHRihEQ0JBQDldPTZ8OjNXeDYvLjMsUCopTScsJSQpIkYmZmUjekB+d191dHl4cTdvV3NycXBpL21sa2QqaGdgZV5dI2FaWV5dXFV5WVhXUE9zU1JRSm4xMEZLRGgrQUZFREM8O18/IT08OzozV3gwNS4tLCtPKU1ubSsqKSInfkQx",0x0A,0x0A,0

bsol   db   "Input the key: ",0

badsol db  "Bad solution",0x0A,0

section .bss
ruser   resb  50
rpass   resb  50

orbuf  resb 928
key resb  100
key1 resb 100

value1  resb  10
value2   resb   10
value3   resb   10

section .text

global _start
_start:





printn o1
newLine

layer1:
printn enterance
printn simple
printn usermsg

readStdin ruser,50

printn passmsg

readStdin rpass,50



strcmp ruser,user

push r9



strcmp rpass,pass

pop rax

add rax,r9

cmp rax,4

je correct

printn badcredsmsg
exit

correct:

printn credsmsg




;;;;;;;;;;;;;;;;;;;;;the openning;;;;;;;;;;;;;;;;;;;;;;;;;;;
printn theopening
printn base64
printn myster
opening:
printn bsol
readStdin key,100

mov r9,0
mov rbx,0
keyl:
cmp r9,0x0A
je h

mov al,byte [key+r9]
add rbx,rax


inc r9
mov rax,0
jmp keyl

h:

cmp rbx,1133
je goodkey
printn bkey
exit
goodkey:
printn gkey

;;;;;;;;;;;;;;;;;;;;;the middlegame;;;;;;;;;;;;;;;;;;;;;;;;;;;
printn themiddlegame
printn rome

middlegame:
printn key1msg
readStdin key1,100

mov r9,0
mov r13,0
mov rax,0
mov rbx,0
key1l:

cmp byte [key1 + r9],0x0A
je fkey1

mov al,byte [key + r9]
mov bl,byte [key1 + r9]

add rax,rbx
mov r12,rax

shr r12,3

mov rax,4
mul r12
mov r12,rax

cmp r12,50
setge cl

cmp r12,102
setle dil


add rcx,rdi
cmp rcx,2
je sum
sum:

add r13,r12

mov rax,0
mov rbx,0
inc r9

jmp key1l

fkey1:

cmp r13,984
je gkey1

printn bkey
exit

gkey1:
printn gkey

;;;;;;;;;;;;;;;;;;;;;the endgame;;;;;;;;;;;;;;;;;;;;;;;;;;;


printn theendgame

mov r14,0
mov r15,0
theloop:
cmp r14,3
je there
readStdin value1,10

atoi value1

mov rax,r9

mul r9
mov rbx,rax
mul r9
mov rcx,rax



mov rax,6063
mul rbx

sub  rcx,rax


mov rax,12253322
mul r9

add rcx,rax

mov rax,8254653240

cmp rcx,rax

je here
inc r14
jmp theloop
here:
inc r15
inc r14
jmp theloop

there:
cmp r15,3
jne lbadsol

printn gsol
exit

lbadsol:

printn badsol

exit
