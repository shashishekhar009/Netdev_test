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

# Run the 'show tech' command
output = net_connect.send_command('show tech')

# Save the output to a file
filename = 'show_tech_output.txt'
with open(filename, 'w') as f:
    f.write(output)

# Print a message indicating where the output is saved
print(f"Output saved to {filename}")

# Disconnect from the device
net_connect.disconnect()
