from argparse import ArgumentParser
import socket
import dns.resolver
import requests
from scapy.all import sr1, IP, ICMP

def main():
    parser = ArgumentParser(prog="Socket Demo and Web API requests Demo")
    parser.add_argument('-n', '--no-ping', action='store_true', help="Just outputs the network information")
    parser.add_argument('-q', '--quiet', action='store_true', help="Only output the results of pinging the user-specified addresses")
    parser.add_argument('-p', '--ping', nargs='+', help="List of addresses to ping")
    args = parser.parse_args()
    
    if args.no_ping:
        print("Just outputs the network information")
        return
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(0)
        sock.connect(('8.8.8.8', 53))
        local_ip = sock.getsockname()[0]
        print(f"Local IP Address: {local_ip}")
    except Exception as e:
        print("Local IP Address could not be determined:", e)
        return
    

    resolver = dns.resolver.Resolver()
    dns_servers = resolver.nameservers
    print(f"DNS Server(s): {dns_servers}")
    
    try:
        response = requests.get('https://api.ipify.org?format=json')
        public_ip = response.json()['ip']
        print(f"Public IP Address: {public_ip}")
    except Exception as e:
        print("Public IP Address could not be determined:")
    
    print("\nPinging ...")
    
    for dns_server in dns_servers:
        icmp_packet = IP(dst=dns_server) / ICMP()
        response = sr1(icmp_packet, timeout=2, verbose=False)
        if response:
            print(f"default DNS Server {dns_server}: OK")
        else:
            print(f"default DNS Server {dns_server}: FAILED")
    
    google_dns_server = '8.8.8.8'
    icmp_packet = IP(dst=google_dns_server) / ICMP()
    response = sr1(icmp_packet, timeout=2, verbose=False)
    if response:
        print("public DNS Server 8.8.8.8: OK")
    else:
        print("public DNS Server 8.8.8.8: FAILED")
    
    if args.ping:
        for device in args.ping:
            icmp_packet = IP(dst=device) / ICMP()
            response = sr1(icmp_packet, timeout=2, verbose=False)
            if response:
                print(f"{device}: OK")
            else:
                print(f"{device}: FAILED")

if __name__ == '__main__':
    main()
