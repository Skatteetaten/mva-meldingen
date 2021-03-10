import requests
from docs.documentation.test.InnsendingServices import printing, Miljo


def last_opp(miljo, url, konvolutt_xml, token):
    payload = bytearray(konvolutt_xml, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/xml',
              'Content-Disposition': 'attachment; filename=konvolutt.xml'}

    response = requests.request("PUT", url, headers=header, data=payload)
    printing(response)
