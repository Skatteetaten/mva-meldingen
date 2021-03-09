import requests
from docs.documentation.test.testinnsending.InnsendingServices import printing, Miljo

local = Miljo.local.name


def last_opp(miljo, url, melding_xml, token):
    if miljo == local:
        url = url.replace('https', 'http')

    payload = bytearray(melding_xml, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'text/xml',
              'Content-Disposition': 'attachment; filename=mva-melding.xml'}

    response = requests.request("POST", url, headers=header, data=payload)
    printing(response)
