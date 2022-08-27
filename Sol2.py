from pwn import * #pip install pwntools
import re
Host="671ea6d7980a39c6.247ctf.com" #change this  accordingly
Port=50407 #change this accordingly
conn = remote(Host,Port)
print(conn.recvline())
print(conn.recvline())
for i in range(500):
    try:
        print("We are at question : {0}".format(i))
        data = conn.recvline().decode("utf-8")
        l = re.findall(r'\d+',data)
        a = int(l[0])
        b = int(l[1])
        ans = (str(a+b)+'\r\n').encode("utf-8")
        conn.sendline(ans)
        conn.recvline()
    except Exception as e:
        print(e)
print(conn.recvline())
conn.close()
