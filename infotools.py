import sys
import requests
import json
import socket

#Read the website URL from the command line 
if len(sys.argv) != 2:
    print("Usage: python infotool.py <websiteurl>")
    sys.exit(1)

website_url = sys.argv[1]

#Getting the ip address 
try:
    ip_address = socket.gethostbyname(website_url)
    print(f"IP Address: {ip_address}")
except socket.gaierror:
    print("Could not get IP address.")
    sys.exit(1)

#Fetching location information
response = requests.get(f"https://ipinfo.io/{ip_address}/json")
if response.status_code == 200:
    location_data = response.json()
    print(json.dumps(location_data, indent=4))
else:
    print("Could not fetch location information.")


# Output IP Address and Location Information
print(f"IP Address: {ip_address}")
if 'loc' in location_data:
    print(f"Location: {location_data['loc']}")
else:
    print("Location information not available.")

