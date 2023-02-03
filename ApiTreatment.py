import requests

response = requests.get(f"http://economia.awesomeapi.com.br/json/last/USD-BRL")
if response.status_code == 200:
    print("Good")
    print(response.json())
    for i in response.json():
        print(i)
else:
    print(f"erro: {response.status_code}")
