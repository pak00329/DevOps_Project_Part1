import requests
endPoint = requests.post("http://127.0.0.1:5000/user/3", json={"userName":"Rob"})
print(endPoint.text)