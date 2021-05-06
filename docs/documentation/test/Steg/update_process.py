import requests
from Steg.FilingServices import printing


def next_step(url, token):
    url = url + "/process/next"
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}

    response = requests.request("PUT", url, headers=header)
    printing(response)
    return response
