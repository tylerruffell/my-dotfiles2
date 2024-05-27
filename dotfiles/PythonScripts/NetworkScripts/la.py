from argparse import ArgumentParser
import requests
from scapy.all import sr1, IP, UDP, DNS, DNSQR
import socket

def main():
    parser = ArgumentParser(prog="Socket Demo and Web API requests Demo")
    parser.add_argument('-i', '--ip', action='store_true')
    parser.add_argument('domain_name')
    args = parser.parse_args()
    hostname = socket.gethostname()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.domain_name, 17)) 
    response = sock.recv(2048) 
    if args.ip:
        local_ip = sock.getsockname()
        print(f"running on host {hostname} with IP {local_ip[0]}")
    else:
        print(f"running on host {hostname}")
    print(f"Quote of the Day: {response.decode('ascii')}")

    response = requests.get('https://api.agify.io/', params={'name' : 'anna'})
    response.raise_for_status()
    data = response.json()
    print(f"Anna's predicted age is {data['age']}")

    print("Resolving 'weber.edu'")
    
    response = sr1(IP(dst="{8.8.8.8}")/UDP()/DNS(rd=1,qd=DNSQR(qname="weber.edu")))
    print(f"Answer: {response}")

if __name__ == '__main__':
    main()
