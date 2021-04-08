import requests
from Steg.SubmissionServices import printing, Environment

local = Environment.local.name


def next_step(environment, url, token):
    url = url + "/process/next"
    if environment == local:
        url = url.replace('https', 'http')

    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}

    response = requests.request("PUT", url, headers=header)
    printing(response)
    return response
