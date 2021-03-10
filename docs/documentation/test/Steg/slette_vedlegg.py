import requests
from Steg.InnsendingServices import printing


def slett_sist_lastet_opp_vedlegg(miljo, url, vedlegg, token):
    payload = bytearray(vedlegg, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'text/xml',
              'Content-Disposition': 'attachment; filename=mva-vedlegg.xml'}

    response = requests.request("DELETE", url, headers=header, data=payload)
    printing(response)
