from netmiko import ConnectHandler
from getpass import getpass

D1 = {
      'device_type': 'cisco_ios',
      'ip': '192.168.234.132',
      'username': 'shashi',
      'password': getpass()
     }

netconnect = ConnectHandler(**D1)
output = netconnect.send_command('show version')
print(output)