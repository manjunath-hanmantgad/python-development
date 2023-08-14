import requests

data = {"sentence": "This is an example sentence"}
response = requests.post("http://127.0.0.1:5000/generate_array", json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print("Error:", response.text)
