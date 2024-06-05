import requests

from main.models import IpInfo


def auto_ip(ip):
    response = requests.get(url=f"http://ip-api.com/json/{ip}?lang=ru")
    result = response.json()
    record = []
    for key, value in result.items():
        record.append(value)
    print(result)
    city = result.get('city')
    country = result.get('country')
    location = f"{result.get('lat')}, {result.get('lon')}"
    postal = result.get('zip')
    print(city, country, location, postal)
    try:
        new_record = IpInfo(ip=ip, city=city, country=country, location=location, postal=postal)
        new_record.save()
    except  Exception as e:
        print(e)
    return result.items
