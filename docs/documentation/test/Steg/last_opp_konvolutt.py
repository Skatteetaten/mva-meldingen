import requests
from docs.documentation.test.InnsendingServices import printing, Miljo

local = Miljo.local.name


def last_opp(miljo, url, konvolutt_xml, token):
    if miljo == local:
        url = url.replace('https', 'http')

    payload = bytearray(konvolutt_xml, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/xml',
              'Content-Disposition': 'attachment; filename=konvolutt.xml'}

    response = requests.request("PUT", url, headers=header, data=payload)
    printing(response)
