import argparse # Even though the book uses optparse argparse is better and more user frinedly
import socket
import threading

def create_parser_and_take_inputs():
    parser = argparse.ArgumentParser(usage='port_scan.py TARGET_HOST -p TARGET_PORTS\nexample: python3 port_scan.py scanme.nmap.org -p 21,80')

    parser.add_argument('tgt_host', type=str, metavar='TARGET_HOST',help='specify target host (IP address or domain name)')
    parser.add_argument('-p', required=True, type=str, metavar='TARGET_PORTS', help='specify target port[s] separated by comma (no spaces)')
    args = parser.parse_args()
    args.tgt_ports = str(args.p).split(',')
    port_scanner(args.tgt_host, args.tgt_ports)


def port_scanner(tgt_host,tgt_ports):
    try:
        target_ip = socket.gethostbyname(tgt_host) # It makes a simple DNS request to find the IP address of the target 
    except Exception as e:
        print(e)
    for port in tgt_ports:
        current_port = threading.Thread(target = conn_scan, args = (tgt_host,int(port)))
        current_port.start()


def conn_scan(tgt_host, tgt_port):
    screen_lock = threading.Semaphore()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_skt:
        try:
            conn_skt.connect((tgt_host, tgt_port))
            conn_skt.send(b'ViolentPython\r\n')
            results = conn_skt.recv(100).decode('utf-8')
            screen_lock.acquire()
            print(f'[+] {tgt_port}/tcp open')
            print(f'   [>] {results}')
        except OSError:
            screen_lock.acquire()
            print(f'[-] {tgt_port}/tcp closed')
        finally:
            screen_lock.release()



if __name__ == "__main__":
    create_parser_and_take_inputs()
