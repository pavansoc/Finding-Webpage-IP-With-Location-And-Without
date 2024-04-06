import socket
import sys
import requests
import json

def get_ip_info(url):
    try:
        ip_address = socket.gethostbyname(url)
        print(f"The IP Address of {url} is: {ip_address}\n")

        req_two = requests.get(f"https://ipinfo.io/{ip_address}/json")
        resp_ = json.loads(req_two.text)

        print(f"Location: {resp_['loc']}")
        print(f"Region: {resp_['region']}")
        print(f"City: {resp_['city']}")
        print(f"Country: {resp_['country']}")
    except socket.gaierror as e:
        print(f"Error: {e}")

# Check if at least one command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python example1.py <URL>")
    sys.exit(1)

# Get the URL from the command-line argument
url_to_scan = sys.argv[1]

# Call the function to retrieve IP information
get_ip_info(url_to_scan)
