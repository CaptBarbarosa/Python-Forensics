import sys
import socket
import scapy
import os


def try_catch():
    socket.setdefaulttimeout(2)
    s=socket.socket()
    try:  #Try-except are the difference between crashing and not crashing. Without this try except block if there is no connection the program stops abruptly
        s.connect(("192.168.95.148",21))
        ans = s.recv(1024)
        print(ans)
    except Exception as e:
        print(e)


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port))
        banner=s.recv(1024)
        return banner
    except:
        return


def checkVulns(banner):
    try:
        f = open("vuln_banner.txt","r")
        for line in f.readlines():
            #print("line.strip('\\n') is:"+ line.strip('\n')+" and banner is:"+banner+" line.strip in banner is: "+ str(line.strip('\n') in banner))
            if line.strip('\n') in banner:
                print(f"The server given:{banner} is vulnerable")
    except Exception as e:
        print(e)


def sys_ex():
    print(f"You have entered {len(sys.argv)} arguments in the terminal an the are")
    for arguments in sys.argv:
        print(arguments)


if __name__ == "__main__":
    checkVulns(" Xitami")
    sys_ex()


