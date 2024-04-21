import re

# Simulated config data as string
config_data = """
interface GigabitEthernet0/1
 ip address 192.168.1.1 255.255.255.0
!
interface GigabitEthernet0/2
 ip address 192.168.2.1 255.255.255.0
!
"""

# Function to find IP addresses
def find_ip_addresses(config):
    ip_pattern = r'ip address (\d+\.\d+\.\d+\.\d+)'
    ips = re.findall(ip_pattern, config)
    return ips

# Using the function
ips = find_ip_addresses(config_data)
print("IP Addresses found:", ips)
