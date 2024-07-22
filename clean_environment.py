import requests

requests.get('http://127.0.0.1:5000/stop_server')
requests.get('http://127.0.0.1:5001/stop_server')

try:
    response = requests.get('http://127.0.0.1:5001/stop_server')
    response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
    print(response.text)  # If needed, print the response text
except requests.exceptions.RequestException as e:
    print("Error: Failed to communicate with the server. Please try again later.")
