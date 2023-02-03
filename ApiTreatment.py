import requests

def GetApi(api):
  response = requests.get(f"{api}")
  if response.status_code == 200:
    print(response.json())
  else:
    print(f"erro: {response.status_code}")

ApiUrl = input(f'Api URL: ')

GetApi(ApiUrl)