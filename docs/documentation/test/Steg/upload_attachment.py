import requests
from Steg.FilingServices import printing


def upload(url, attachment, content_type, token):
    with open("./eksempler/" + attachment, 'rb') as file:
        payload = file.read()
    header = {'Authorization': 'Bearer ' + token, 'content-type': content_type,
              'Content-Disposition': 'attachment; filename=' + attachment}

    response = requests.request("POST", url, headers=header, data=payload)
    printing(response)

    return response
