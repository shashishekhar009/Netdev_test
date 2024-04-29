import json

# Python dictionary
router_data = {
    "name": "Router1",
    "interfaces": [
        {"name": "Gig0/1", "ip": "192.168.1.1"}
    ]
}

# Convert to JSON string
json_str = json.dumps(router_data, indent = 4)
print(json_str)

# Write JSON to a file
with open('output_config.json', 'w') as file:
    json.dump(router_data, file, indent=4)
