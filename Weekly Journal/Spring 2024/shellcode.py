from pwn import *
from pwnlib import shellcraft

context.arch = 'amd64'  
context.os = 'linux'    

# 32 bit architecture
#shellcode_asm = shellcraft.i386.linux.sh()

# 64 bit architecture
shellcode_asm =  shellcraft.amd64.linux.sh()
print('Assembly Code for Executing a Shell:\n' + shellcode_asm)

# Assemble the shellcode to get the bytes
shellcode = asm(shellcode_asm)

print('---------------------')

#Print the generated shellcode in hexadecimal format
print(enhex(shellcode))
