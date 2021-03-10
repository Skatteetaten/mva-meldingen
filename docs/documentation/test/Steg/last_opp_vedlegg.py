import requests
from Steg.InnsendingServices import printing


def last_opp(miljo, url, vedlegg, content_type, token):
    with open("./eksempler/" + vedlegg, 'rb') as file:
        payload = file.read()
    header = {'Authorization': 'Bearer ' + token, 'content-type': content_type,
              'Content-Disposition': 'attachment; filename=' + vedlegg}

    response = requests.request("POST", url, headers=header, data=payload)
    printing(response)

    return response
