import requests
from Steg.FilingServices import printing


def create(domain, token, app, org_number):
    url = domain + app + "/instances/"
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}
    payload = "{'instanceOwner': {'organisationNumber': " + org_number + "}}"
    instance = requests.request("POST", url, headers=header, data=payload)
    printing(instance)

    return instance.json()
