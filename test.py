import requests
endPoint = requests.post("http://127.0.0.1:5000/users/2", json={"user_name":"Robert"})
print(endPoint.text)