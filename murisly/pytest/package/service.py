#!/usr/bin/python3.2
# a small service

import socket

s = socket.socket()

host = socket.gethostname();
print("host is :" + host);
port = 1234;
s.bind((host, port));

s.listen(5)
print("service start!")
while True:
    c, addr = s.accept();
    print('...connect from', addr);
    c.send(("this is ubuntu").encode())
    c.close();

print("service end");
