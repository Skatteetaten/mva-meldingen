import requests
from docs.documentation.test.InnsendingServices import printing, Miljo

local = Miljo.local.name


def hent(miljo, url, token):
    if miljo == local:
        url = url.replace('https', 'http')

    header = {'Authorization': 'Bearer ' + token}
    instans = requests.request("GET", url, headers=header)
    printing(instans)

    return instans.json()
