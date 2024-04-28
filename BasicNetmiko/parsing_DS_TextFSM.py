from netmiko import ConnectHandler
from getpass import getpass
import textfsm

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

# Path to the TextFSM template file
template_file_path = "show_ip_int_brief.template"

# Load the TextFSM template file
with open(template_file_path) as f:
    template = textfsm.TextFSM(f)

# Parse the output using the template
parsed_data = template.ParseText(output)

# Print the parsed data
for entry in parsed_data:
    print(dict(zip(template.header, entry)))

# Close the connection
net_connect.disconnect()
