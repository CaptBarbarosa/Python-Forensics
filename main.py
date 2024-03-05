import socket
import scapy
if __name__ == '__main__':
    socket.setdefaulttimeout(2)
    s=socket.socket()
    s.connect(("192.168.95.148",21))
    ans = s.recv(1024)
    print(ans)
