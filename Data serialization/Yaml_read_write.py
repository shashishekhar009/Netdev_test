import yaml

def read_yaml(file_path):
    """Read a YAML file and return the data."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(data, file_path):
    """Write data to a YAML file."""
    with open(file_path, 'w') as file:
        yaml.dump(data, file, indent=4)

# Path to the YAML file
file_path = 'router_config.yaml'

# Read the router configuration
config = read_yaml(file_path)
print("Original Configuration:", config)

# Modify the configuration
config['router']['hostname'] = 'Router2'
config['router']['interfaces'][0]['ip_address'] = '192.168.10.1'

# Write the modified configuration to a new file
new_file_path = 'modified_router_config.yaml'
write_yaml(config, new_file_path)
print("Modified configuration written to", new_file_path)