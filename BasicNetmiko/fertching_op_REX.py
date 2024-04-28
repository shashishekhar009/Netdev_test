from netmiko import ConnectHandler
from getpass import getpass

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
output = net_connect.send_command_timing('show version', delay_factor=2)
print(output)

output1 = net_connect.send_command_timing('show ip arp', delay_factor=2)
print(output1)

# Disconnect from the device
net_connect.disconnect()
