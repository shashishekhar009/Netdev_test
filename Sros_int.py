from netmiko import ConnectHandler

sros_l3 = {
    'device_type': 'alcatel_sros',  # This specifies the device type for Nokia SR OS
    'ip': '10.0.0.90',            # Replace with the IP address of your Nokia device
    'username': 'admin',         # Replace with your username
    'password': 'admin'        # Replace with your password
}

net_connect = ConnectHandler(**sros_l3)

# Send command to show router interface details
output = net_connect.send_command('show router interface')
print(output)

# Disconnect from the device
net_connect.disconnect()