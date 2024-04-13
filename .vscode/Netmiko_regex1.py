from netmiko import ConnectHandler
from getpass import getpass 
import re

# List of device IP addresses
device_list = ["192.168.234.132"]

for ip in device_list:
    # Device connection configuration
    cisco = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "shashi",
        "password": getpass("Enter your password for device {}: ".format(ip))  # Prompt for password securely
    }
    
    # Connect to the device
    net_connect = ConnectHandler(**cisco)
    
    # Send the 'show version' command and store the output
    output = net_connect.send_command("show version")
    
    # Use regex to search for the version pattern in the command output
    # Adjusted regex to account for potential formatting variations
    match = re.search(r'Cisco IOS Software,\s*Linux Software.*?Version\s*(\d+\.\d+\(\d+\)[A-Z]?\d+\.\d+)', output, re.DOTALL)
    
    # If a match is found, extract and print the version information
    if match:
        version = match.group(1)  # Extracts only the version number, e.g., "15.2(4)M5.3"
        print(f"Version on device {ip}: {version}")
    else:
        print(f"No version information found in output from device {ip}.")
    
    # Disconnect from the device
    net_connect.disconnect()

