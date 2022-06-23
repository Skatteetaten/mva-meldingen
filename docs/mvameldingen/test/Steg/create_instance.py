import requests


def create(domain, token, app, org_number):
    url = domain + app + "/instances/"
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}
    payload = "{'instanceOwner': {'organisationNumber': " + org_number + "}}"
    instance = requests.request("POST", url, headers=header, data=payload)

    print("status code:", instance.status_code)
    print("reason:", instance.reason)
    print("headers:", instance.headers)
    print("content:", instance.content.decode("utf-8"), "\n")

    return instance.json()
