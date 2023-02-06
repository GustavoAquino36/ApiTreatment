import requests

def GetApi(api):
  response = requests.get(f"{api}")
  if response.status_code == 200:
    if (len(response.json())) >= 2:
      for i in response.json():
        print(i)
        print(response.json()[i])
    else:
      print(response.json())
  else:
    print(f"erro: {response.status_code}")

ApiUrl = input(f'Api URL: ')

GetApi(ApiUrl)