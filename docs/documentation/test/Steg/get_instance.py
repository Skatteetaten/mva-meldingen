import requests


def get(url, token):
    header = {'Authorization': 'Bearer ' + token}
    instance = requests.request("GET", url, headers=header)

    print("status code:", instance.status_code)
    print("reason:", instance.reason)
    print("headers:", instance.headers)
    print("content:", instance.content.decode("utf-8"), "\n")

    return instance.json()


def get_data(url, token):
    header = {'Authorization': 'Bearer ' + token}
    request = requests.request("GET", url, headers=header)

    return request
