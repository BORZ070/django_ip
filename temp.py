import requests


url_api = 'https://ipinfo.io/5.144.118.218?token=aef11aa0e1c15e'


def api_connecting():
    connect = requests.get(url_api)
    print(connect.status_code)
    print(connect.json())

api_connecting()
