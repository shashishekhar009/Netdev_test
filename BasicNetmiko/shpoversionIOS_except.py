from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from getpass import getpass

D1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.234.132',
    'username': 'shashi',
    'password': getpass()
}

try:
    netconnect = ConnectHandler(**D1)
    output = netconnect.send_command('show version')
    print(output)
except NetmikoTimeoutException:
    print("Connection timed out.")
except NetmikoAuthenticationException:
    print("Authentication failed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    netconnect.disconnect()