import requests
from docs.documentation.test.InnsendingServices import printing, Miljo

local = Miljo.local.name


def last_opp(miljo, url, vedlegg, content_type, token):
    if miljo == local:
        url = url.replace('https', 'http')

    with open("./eksempler/" + vedlegg, 'rb') as file:
        payload = file.read()
    header = {'Authorization': 'Bearer ' + token, 'content-type': content_type,
              'Content-Disposition': 'attachment; filename=' + vedlegg}

    response = requests.request("POST", url, headers=header, data=payload)
    printing(response)

    return response
