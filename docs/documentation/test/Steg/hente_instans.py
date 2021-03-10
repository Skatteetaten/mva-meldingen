import requests
from docs.documentation.test.InnsendingServices import printing, Miljo


def hent(miljo, url, token):
    header = {'Authorization': 'Bearer ' + token}
    instans = requests.request("GET", url, headers=header)
    printing(instans)

    return instans.json()
