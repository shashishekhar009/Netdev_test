import os

# Function to simulate ping to a host
def ping_host(host):
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        print(f"{host} is up!")
    else:
        print(f"{host} is down!")

# Using the function
ping_host('google.com')

# check with Su access