import socket

def scan_ports(target, ports):
    open_ports = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        try:
            sock.connect((target, port))
            open_ports.append(port)
            sock.close()
        except (socket.timeout, ConnectionRefusedError):
            pass
    
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter target host: ")
    target_ports = input("Enter target ports (comma-separated or range, e.g., 80,443 or 20-80): ")

    try:
        target_ports = target_ports.split(',')
        ports_to_scan = []

        for port in target_ports:
            if '-' in port:
                start, end = map(int, port.split('-'))
                ports_to_scan.extend(range(start, end + 1))
            else:
                ports_to_scan.append(int(port))

        open_ports = scan_ports(target_host, ports_to_scan)

        if open_ports:
            print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")
        else:
            print(f"No open ports found on {target_host}")
    except ValueError:
        print("Invalid input. Please use a comma-separated list or range for ports.")
