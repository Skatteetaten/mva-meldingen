import requests
from Steg.SubmissionServices import printing


def get(url, token):
    header = {'Authorization': 'Bearer ' + token}
    instance = requests.request("GET", url, headers=header)
    printing(instance)

    return instance.json()
