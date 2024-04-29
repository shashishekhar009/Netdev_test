from netmiko import ConnectHandler
from getpass import getpass
import yaml

# Function to save data to a YAML file
def save_to_yaml(data, filename):
    with open(filename, 'w') as file:
        yaml.dump(data, file)

# Device details
device_ios = {
    "device_type": "cisco_ios",
    "ip": "192.168.234.132",
    "username": "shashi",
    "password": getpass("Enter password: "),  # Securely input password
}

# Connect to the device
net_connect = ConnectHandler(**device_ios)

# Dictionary to hold command outputs
command_outputs = {}

# Run commands with delay between each command
command_outputs['show_version'] = net_connect.send_command_timing('show version', delay_factor=2)
command_outputs['show_ip_arp'] = net_connect.send_command_timing('show ip arp', delay_factor=2)

# Print the outputs
for command, output in command_outputs.items():
    print(f"Output of '{command}':\n{output}\n")

# Disconnect from the device
net_connect.disconnect()

# Save command outputs to a YAML file
save_to_yaml(command_outputs, 'router_commands_output.yaml')
