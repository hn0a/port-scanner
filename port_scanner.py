import socket
import os
import sys
import argparse
from datetime import datetime
from colorama import init, Fore, Style

def scan_ports(remote_server_ip, verbose):
    print('-' * 60)
    print(f"Starting the scan of the machine {remote_server_ip}")
    print('-' * 60)

    # Record the start time of the scan
    start_time = datetime.now()

    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Timeout to avoid hanging on closed ports
            result = sock.connect_ex((remote_server_ip, port))
            if result == 0:
                print(Fore.GREEN + f"Port {port}: Open" + Style.RESET_ALL)
            elif verbose:
                print(Fore.RED + f"Port {port}: Closed" + Style.RESET_ALL)
            sock.close()

    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()

    except socket.error:
        print("\nCouldn't connect to the server.")
        sys.exit()

    # Record the end time of the scan
    end_time = datetime.now()

    # Calculate the total time taken for the scan
    total_time = end_time - start_time

    print('-' * 60)
    print(f"Scan completed in: {total_time}")
    print('-' * 60)

def main():
    parser = argparse.ArgumentParser(description="A simple port scanner.")
    parser.add_argument("ip", nargs='?', help="The IP address of the server to scan.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity, show closed ports.", action="store_true")
    args = parser.parse_args()

    # Clear the screen
    os.system('clear')

    # If IP address is not provided as an argument, prompt the user to enter it
    if not args.ip:
        args.ip = input("Enter the IP address of the server to scan: ")

    # Initialize colorama
    init(autoreset=True)

    # Call the port scanning function
    scan_ports(args.ip, args.verbose)

if __name__ == "__main__":
    main()
