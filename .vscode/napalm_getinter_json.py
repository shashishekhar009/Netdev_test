from napalm import get_network_driver
import json

driver = get_network_driver("ios")
device = driver("192.168.234.132", "shashi", "shashi90")
device.open()
print(json.dumps(device.get_interfaces_ip(), indent=2))
device.close()