import requests
from docs.documentation.test.testinnsending.InnsendingServices import printing


def oprett(domene, token, app, org_nummer):
    url = domene + app + "/instances/"
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}
    payload = "{'instanceOwner': {'organisationNumber': " + org_nummer + "}}"
    instans = requests.request("POST", url, headers=header, data=payload)
    printing(instans)

    return instans.json()
