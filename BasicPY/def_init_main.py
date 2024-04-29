from netmiko import ConnectHandler
from getpass import getpass

def Device():
    try:
        D1 = {
            'device_type': 'cisco_ios',
            'ip': '192.168.234.132',
            'username': 'shashi',
            'password': getpass('Enter the password: ')
        }

        Net_connect = ConnectHandler(**D1)

        commands = ['show version', 'show ip route', 'show ip arp']

        for command in commands:
            output = Net_connect.send_command(command)
            print(f"Command: {command}\nOutput:\n{output}\n{'='*50}")

        # Disconnect from the device
        Net_connect.disconnect()
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the Device function
if __name__ == "__main__":
    Device()