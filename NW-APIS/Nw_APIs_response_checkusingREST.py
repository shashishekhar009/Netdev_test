import requests
import json

def get_data_from_api(url):
    # Make the API request
    response = requests.get(url)
    
    # Check the HTTP response status codes to handle different outcomes
    if response.status_code == 200:
        # Success: parse the JSON response and return the data
        data = response.json()
        # Save the data to a JSON file
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        return data
    elif response.status_code == 404:
        # Resource not found
        print("Resource not found.")
    elif response.status_code == 401:
        # Unauthorized access
        print("Authorization failed. Check your credentials or permissions.")
    elif response.status_code == 500:
        # Server error
        print("Server error. Please try again later.")
    else:
        # Other unexpected errors
        print(f"Failed to retrieve data. Status code: {response.status_code}")
    return None

# Example URL to a public API (placeholder, replace with your actual API URL)
url = 'https://jsonplaceholder.typicode.com/posts'

# Fetch and store data
data = get_data_from_api(url)
if data:
    print("Data retrieved and saved to 'data.json'.")
else:
    print("No data available.")
