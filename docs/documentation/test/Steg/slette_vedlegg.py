import requests
from docs.documentation.test.testinnsending.InnsendingServices import printing, Miljo

local = Miljo.local.name


def slett_sist_lastet_opp_vedlegg(miljo, url, vedlegg, token):
    if miljo == local:
        url = url.replace('https', 'http')

    payload = bytearray(vedlegg, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'text/xml',
              'Content-Disposition': 'attachment; filename=mva-vedlegg.xml'}

    response = requests.request("DELETE", url, headers=header, data=payload)
    printing(response)
