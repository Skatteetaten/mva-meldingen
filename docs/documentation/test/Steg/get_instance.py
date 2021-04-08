import requests
from Steg.SubmissionServices import printing, Environment

local = Environment.local.name


def get(environment, url, token):
    if environment == local:
        url = url.replace('https', 'http')

    header = {'Authorization': 'Bearer ' + token}
    instance = requests.request("GET", url, headers=header)
    printing(instance)

    return instance.json()
