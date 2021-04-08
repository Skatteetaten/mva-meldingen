import requests
from Steg.SubmissionServices import printing, Environment

local = Environment.local.name


def upload(environment, url, attachment, content_type, token):
    if environment == local:
        url = url.replace('https', 'http')

    with open("./eksempler/" + attachment, 'rb') as file:
        payload = file.read()
    header = {'Authorization': 'Bearer ' + token, 'content-type': content_type,
              'Content-Disposition': 'attachment; filename=' + attachment}

    response = requests.request("POST", url, headers=header, data=payload)
    printing(response)

    return response
