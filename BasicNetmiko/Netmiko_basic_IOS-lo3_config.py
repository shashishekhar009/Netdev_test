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

# Configuration commands
config_commands = [
    'interface Loopback3',
    'ip address 3.3.3.3 255.255.255.255'
]

# Send configuration commands
output = net_connect.send_config_set(config_commands)

# Print the output
print(output)

# Disconnect from the device
net_connect.disconnect()
