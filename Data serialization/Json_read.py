import json

# JSON string
json_string = '{"name": "Router1", "interfaces": [{"name": "Gig0/1", "ip": "192.168.1.1"}]}'

# Parse JSON from a string
data = json.loads(json_string)
print(data)

# Parse JSON from a file
with open('config.json', 'r') as file:
    data = json.load(file)
print(data)
