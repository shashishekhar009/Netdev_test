from napalm import get_network_driver
import json

driver = get_network_driver("ios")
device = driver("192.168.234.132", "shashi", "shashi90")
device.open()
print(device.get_config()["running"])
device.close()