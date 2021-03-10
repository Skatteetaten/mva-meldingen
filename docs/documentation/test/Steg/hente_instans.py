import requests
from Steg.InnsendingServices import printing


def hent(miljo, url, token):
    header = {'Authorization': 'Bearer ' + token}
    instans = requests.request("GET", url, headers=header)
    printing(instans)

    return instans.json()
