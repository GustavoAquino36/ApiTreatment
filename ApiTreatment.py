import requests

def GetApi(api):
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print(response.json())
        virgula = str(response.json()).split(',')
        for i in virgula:
            print(i)
    else:
        print(f"erro: {response.status_code}")

ApiUrl = input(f'Api URL: ')

GetApi(ApiUrl)