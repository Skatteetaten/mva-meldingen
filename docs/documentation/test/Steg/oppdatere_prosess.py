import requests
from docs.documentation.test.InnsendingServices import printing, Miljo


def neste(miljo, url, token):
    url = url + "/process/next"
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}

    response = requests.request("PUT", url, headers=header)
    printing(response)
    return response
