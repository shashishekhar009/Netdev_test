from netmiko import ConnectHandler
from getpass import getpass
import xml.etree.ElementTree as ET

# Function to save data to an XML file
def save_to_xml(data, filename):
    root = ET.Element('router_data')
    for command, output in data.items():
        command_element = ET.SubElement(root, command)
        command_element.text = output
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='unicode', xml_declaration=True)

# Device details
device_ios = { 
    "device_type": "cisco_ios",
    "ip": "192.168.234.132",
    "username": "shashi",
    "password": getpass("Enter password: "),  # Prompt for password securely
}

# Connect to the device
net_connect = ConnectHandler(**device_ios)

# Run commands
output_version = net_connect.send_command('show version')
output_arp = net_connect.send_command('show ip arp')

# Disconnect from the device
net_connect.disconnect()

# Structure the data as a dictionary
router_data = {
    "show_version": output_version,
    "show_ip_arp": output_arp
}

# Save the output to an XML file
xml_filename = 'router_output.xml'
save_to_xml(router_data, xml_filename)

print(f"The output has been saved to {xml_filename}")