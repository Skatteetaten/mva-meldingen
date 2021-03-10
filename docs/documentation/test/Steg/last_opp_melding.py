import requests
from docs.documentation.test.InnsendingServices import printing, Miljo


def last_opp(miljo, url, melding_xml, token):
    payload = bytearray(melding_xml, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'text/xml',
              'Content-Disposition': 'attachment; filename=mva-melding.xml'}

    response = requests.request("POST", url, headers=header, data=payload)
    printing(response)
