import socket
from scapy.all import IP, TCP, sr1

from model.ports_class import PortsReport

def scan_port_range(target, ports, timeout=3):
    open_ports = []
    closed_ports = []

    print(f"Scanning Target    : {target}")

    for port in ports:
        response = sr1(IP(dst=target) / TCP(dport=port, flags="S"), timeout=timeout, verbose=False)
        if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            open_ports.append(port)
        else:
            closed_ports.append(port)

    return PortsReport(open_ports, closed_ports);

def scan_port_on_url(url, ports):
    try:
        ip = socket.gethostbyname(url)
        print(f"Resolved {url} to IP address: {ip}")
        return scan_port_range(ip, ports);
    except socket.error as e:
        print(f"Error resolving domain name: {e}")
        return None