from netmiko import ConnectHandler
from getpass import getpass

Device1 = {
    'ip' : '192.168.234.132',
    'device_type' : "cisco_ios",
    'username' : 'shashi',
    'password' : getpass()
}

Net_connect = ConnectHandler(**Device1)

commands = [ 'interface loopback3', 'ip address 3.3.3.3 255.255.255.255']

output = Net_connect.send_config_set(commands)

print(output)

Net_connect.disconnect()