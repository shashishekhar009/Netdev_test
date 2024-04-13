from napalm import get_network_driver
import json
from getpass import getpass 

driver = get_network_driver("ios")
device = driver("192.168.234.132", "shashi", getpass())
device.open()
print(device.get_config()["running"])
device.close()