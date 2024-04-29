import xml.etree.ElementTree as ET

# XML string
xml_data = """
<router>
    <hostname>Router1</hostname>
    <interfaces>
        <interface>
            <name>Gig0/1</name>
            <ip>192.168.1.1</ip>
        </interface>
    </interfaces>
</router>
"""

# Parse XML from a string
root = ET.fromstring(xml_data)

# Accessing an element
hostname = root.find('hostname').text
print(hostname)
 