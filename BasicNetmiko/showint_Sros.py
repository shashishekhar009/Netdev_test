from netmiko import ConnectHandler

sros_l3 = {
    'device_type': 'alcatel_sros',  # This specifies the device type for Nokia SR OS
    'ip': '10.0.0.90',            # Replace with the IP address of your Nokia device
    'username': 'admin',         # Replace with your username
    'password': 'admin'        # Replace with your password
}