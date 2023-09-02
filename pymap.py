import nmap
import argparse

def scan_ports(ip, port_set):
    scanner = nmap.PortScanner()
    for port in port_set:
        response = scanner.scan(ip, str(port))
        res = response["scan"][ip]["tcp"][int(port)]
        state = res["state"]
        service = res["name"]
        print(f"Port {port} is {state}. / Service: {service}")

def main():
    parser = argparse.ArgumentParser(description="Python Nmap medium.")
    parser.add_argument("-t", metavar="Target", help="Target address.")
    parser.add_argument("--scan-type", choices=["fast", "med", "top", "normal", "full"], metavar="Scan Type", \
                        help="Choose what type of scan you would like.")
    args = parser.parse_args()

    ip = args.t
    scan_type = args.scan_type

    if scan_type == "fast":
        port_set = [20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443,
                    445, 554, 587, 993, 995, 1723, 3306, 3389, 5900, 8008, 8080]
    elif scan_type == "med":
        port_set = [20, 21, 22, 23, 25, 53, 69, 79, 80, 88, 110,
                    111, 135, 139, 143, 161, 389, 443, 445, 512, 513,
                    514, 515, 548, 623, 626, 631, 873, 1025, 1110, 1433,
                    1521, 1720, 1723, 2049, 2100, 2401, 2483, 3306, 3389, 5432,
                    5800, 5900, 5984, 6379, 6660, 6661, 6662, 6663, 6664, 6665]
    elif scan_type == "top":
        port_set = [20, 21, 22, 23, 25, 53, 69, 79, 80, 88, 110,
                    111, 135, 139, 143, 161, 389, 443, 445, 512, 513,
                    514, 515, 548, 623, 626, 631, 873, 1025, 1110, 1433,
                    1521, 1720, 1723, 2049, 2100, 2401, 2483, 3306, 3389, 5432,
                    5800, 5900, 5984, 6379, 6660, 6661, 6662, 6663, 6664, 6665,
                    6666, 6667, 6668, 6669, 7000, 7001, 7002, 7003, 7004, 7005,
                    7006, 7007, 7008, 7009, 7010, 8000, 8008, 8009, 8010, 8011,
                    8080, 8081, 8443, 8888, 9090, 9100, 9999, 10000, 32768, 32769,
                    32770, 32771, 32772, 32773, 32774, 32775, 32776, 32777, 32778, 32779,
                    49152, 49153, 49154, 49155, 49156, 49157, 49158, 49159, 49160, 49161,
                    49163, 49165, 49167, 49175, 49176, 50389, 5666, 11211, 27017, 50070]
    elif scan_type == "normal":
        port_set = range(1, 1001)
    elif scan_type == "full":
        port_set = range(1, 65536)

    scan_ports(ip, port_set)


if __name__ == "__main__":
    main()




