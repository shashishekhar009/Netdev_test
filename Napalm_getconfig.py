# Import necessary modules
import napalm
from getpass import getpass

def main():
    # Device configuration
    device_config = {
        'hostname': '192.168.234.132',  # Replace with your device's IP address
        'username': 'shashi',           # Replace with your device's login username
        'password': getpass ()
     }

    # Get the device type from the user (e.g., 'ios', 'iosxr', 'junos', etc.)
    device_type = 'ios'

    # Load the appropriate NAPALM driver for the device
    driver = napalm.get_network_driver(device_type)

    # Use the driver to create a connection object
    device = driver(**device_config)

    try:
        # Open the connection to the device
        device.open()
        
        # Fetch the running configuration
        config = device.get_config()
        print("Running Config:\n", config['running'])
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Always ensure the connection is closed
        device.close()

if __name__ == "__main__":
    main()