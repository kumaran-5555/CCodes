#!/usr/bin/python
__author__ = 'kumaran'

import socket
import sys
import fileinput

if len(sys.argv) != 3:
    print("Usage: "+sys.argv[0]+" <hostName> <hostPort>")
    sys.exit(1)


hostname = sys.argv[1]
port = sys.argv[2]

# connect to server
soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM )
soc.setsockopt(socket.IPPROTO_TCP, socket.SO_RCVBUF, 55555)

hostIp = socket.gethostbyname(hostname)
print(hostIp, hostname)
conn = soc.connect((hostIp, int(port)))

try:

    while True:
        line = sys.stdin.readline()
        soc.send(bytes(line, encoding="utf-8"))

except KeyboardInterrupt:
    soc.close()





