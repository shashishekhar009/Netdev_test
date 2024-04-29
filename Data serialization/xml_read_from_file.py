

# Parse XML from a file
tree = ET.parse('config.xml')
root = tree.getroot()

# Accessing an element
hostname = root.find('hostname').text
print(hostname)

