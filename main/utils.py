import requests
from django.shortcuts import redirect

from main.models import IpInfo


def auto_ip(ip):
    response = requests.get(url=f"http://ip-api.com/json/{ip}?lang=ru")
    result = response.json()
    # record = []
    # for key, value in result.items():
    #     record.append(value)
    print(result)
    # try:
    #     IpInfo.objects.create(ip=ip, city=result.get('city'), country=result.get('country'),
    #                           location=f"{result.get('lat')}, {result.get('lon')}", postal=result.get('zip'))
    # except Exception as e:
    #     print(e)
    # return result.items

    if result.get('status') == 'success' and response.status_code == 200:
        IpInfo.objects.create(ip=ip, city=result.get('city'), country=result.get('country'),
                              location=f"{result.get('lat')}, {result.get('lon')}", postal=result.get('zip'))
        return result
    else:
        # return redirect('error/')
        return ('NOT FOUND IP')
