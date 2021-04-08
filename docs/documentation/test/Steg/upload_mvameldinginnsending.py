import requests
from Steg.SubmissionServices import printing, Environment

local = Environment.local.name


def upload(environment, url, konvolutt_xml, token):
    if environment == local:
        url = url.replace('https', 'http')

    payload = bytearray(konvolutt_xml, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/xml',
              'Content-Disposition': 'attachment; filename=konvolutt.xml'}

    response = requests.request("PUT", url, headers=header, data=payload)
    printing(response)
