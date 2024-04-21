from netmiko import ConnectHandler

D1 = { 
      'device_type': "cisco_ios",
      'username': "shashi",
      'password': "shashi90",
      'ip': "192.168.234.132"
      }

Net_connect = ConnectHandler(**D1)
filename = "Ios-precheck.txt"
with open (filename, 'r') as file:
    commands = file.read()
    
for cmd in commands:
    output = Net_connect.send_command(cmd)
    
    print (f"output of '{cmd}':\n{output}\n")