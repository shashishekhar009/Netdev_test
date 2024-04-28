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

# Extract interface information into a list of lists
interface_list = [line.split() for line in output_lines]

# Print the extracted interface list
pprint(interface_list)

print(interface_list[2][:4])

# Close the connection
net_connect.disconnect()


