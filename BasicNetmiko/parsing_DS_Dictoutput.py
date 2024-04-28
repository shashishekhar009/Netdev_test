from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Device details
device_ios = { 
    "device_type": "cisco_ios",
    "ip": "192.168.234.132",
    "username": "shashi",
    "password": getpass("Enter password: "),
}

# Connect to the device
net_connect = ConnectHandler(**device_ios)

# Run commands with delay between each command
output = net_connect.send_command('show ip int brief')

# Split the output into lines
output_lines = output.strip().split('\n')

# Extract column headers
headers = output_lines[0].split()

# Initialize list to store dictionaries
interface_list = []

# Parse each line into a dictionary
for line in output_lines[1:]:
    values = line.split()
    interface_dict = {headers[i]: values[i] for i in range(len(headers))}
    interface_list.append(interface_dict)

# Print the extracted interface list
pprint(interface_list)

# Access the value associated with the key 'Interface' in the first dictionary
print(interface_list[0]['Interface'])

# Access the value associated with the key 'IP-Address' in the second dictionary
print(interface_list[1]['IP-Address'])

# Access all keys of the second dictionary
print(interface_list[1].keys())

# Access all values of the second dictionary
print(interface_list[1].values())

# Access a specific value by its index in the values list
print(list(interface_list[1].values())[0])

# Close the connection
net_connect.disconnect()
