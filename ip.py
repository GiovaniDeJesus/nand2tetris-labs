import re
import socket

# Define regular expression patterns for IP addresses, URLs, and IP with port
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
url_pattern = r'https?://\S+'
ip_with_port_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}\b'

# Read the list from a text file (change 'input.txt' to the actual file name)
with open('input.txt', 'r') as file:
    text = file.read()

# Find all matches for IP addresses, URLs, and IP with port
ip_addresses = re.findall(ip_pattern, text)
urls = re.findall(url_pattern, text)
ip_with_ports = re.findall(ip_with_port_pattern, text)

# Resolve IP addresses or domains along with port numbers
resolved_entries = []

for entry in ip_addresses:
    try:
        hostname = socket.gethostbyaddr(entry)[0]
    except socket.herror:
        hostname = 'N/A'
    resolved_entries.append((entry, hostname))

for entry in urls:
    hostname = entry.split('//')[1].split('/')[0]
    resolved_entries.append((entry, socket.gethostbyname(hostname)))

for entry in ip_with_ports:
    parts = entry.split(':')
    hostname = parts[0]
    port = parts[1]
    try:
        ip = socket.gethostbyname(hostname)
        resolved_entries.append((entry, ip + ':' + port))
    except socket.herror:
        resolved_entries.append((entry, 'N/A'))

# Print the resolved entries
for entry, resolved in resolved_entries:
    print(f"{entry} resolves to {resolved}")
