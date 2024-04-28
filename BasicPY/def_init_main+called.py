# Import the Device function from netmiko_script
from def_init_main import Device

def main():
    try:
        # Call the Device function
        Device()
        print("Script execution completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 