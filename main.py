from util.report_formatter import generate_report
from util.scanner import scan_port_on_url, scan_port_range

if __name__ == "__main__":
    print("Choose Scanning Machanism >> ")
    print("\t1. Scan Selected Ports on IP\n\t2. Scan Port Range on IP\n\t3. Scan Selected Ports on URL\n\t4. Scan Port Range on URL")
    scan_machanism = input("Enter your Choice : ")

    match scan_machanism:
        case "1":
            target_ip = input("Enter Target IP Address: ")
            port_range = input("Enter Port Range (e.g., 433, 1532, 80, 88): ")

            ports = map(int, port_range.split(','))

            report = scan_port_range(target_ip, ports)
            generate_report(report)
        case "2":
            target_ip = input("Enter target IP address: ")
            port_range = input("Enter port range (e.g., 1-100): ")

            start_port, end_port = map(int, port_range.split('-'))
            ports = range(start_port, end_port + 1)

            report = scan_port_range(target_ip, ports)
            generate_report(report)
        case "3":
            target_url = input("Enter target URL (e.g., www.example.com): ")
            port_range = input("Enter Port Range (e.g., 433, 1532, 80, 88): ")

            ports = map(int, port_range.split(','))

            report = scan_port_on_url(target_url, ports);
            generate_report(report);
        case "4":
            target_url = input("Enter target URL (e.g., www.example.com): ")
            port_range = input("Enter port range (e.g., 1-100): ")

            start_port, end_port = map(int, port_range.split('-'))
            ports = range(start_port, end_port + 1)

            report = scan_port_on_url(target_url, ports);
            generate_report(report);
        case _:
            print("Invalid Input!, Program Aborted")