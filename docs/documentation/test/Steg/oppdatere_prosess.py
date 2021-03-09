import requests
from docs.documentation.test.testinnsending.InnsendingServices import printing, Miljo

local = Miljo.local.name


def neste(miljo, url, token):
    url = url + "/process/next"
    if miljo == local:
        url = url.replace('https', 'http')

    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}

    response = requests.request("PUT", url, headers=header)
    printing(response)
    return response
