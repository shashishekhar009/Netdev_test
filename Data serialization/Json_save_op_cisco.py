from netmiko import ConnectHandler
from getpass import getpass
import json

# Device details
device_ios = { 
    "device_type": "cisco_ios",
    "ip": "192.168.234.132",
    "username": "shashi",
    "password": getpass("Enter password: "),  # Prompt for password securely
}

# Connect to the device
net_connect = ConnectHandler(**device_ios)

# Run commands with delay between each command
output = net_connect.send_command('show version')
output_arp = net_connect.send_command('show ip arp')

# Disconnect from the device
net_connect.disconnect()

# Structure the data as a dictionary
router_data = {
    "show_version": output,
    "show_ip_arp": output_arp
}

# Define the filename for the JSON output
json_filename = 'router_output.json'

# Write the dictionary to a JSON file
with open(json_filename, 'w') as json_file:
    json.dump(router_data, json_file, indent=4)

print(f"The output has been saved to {json_filename}")
