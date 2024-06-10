import requests


url_api = 'http://127.0.0.1:8000/api/post-ip'


def api_connecting(ip):
    body = {"ip": ip}
    connect = requests.post(url_api, json=body)
    print(connect.status_code)
    print(connect.json())


api_connecting(ip='5.144.118.218')
