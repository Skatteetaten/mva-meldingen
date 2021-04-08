import requests
from Steg.SubmissionServices import printing, Environment

local = Environment.local.name


def upload(environment, url, melding_xml, token):
    if environment == local:
        url = url.replace('https', 'http')

    payload = bytearray(melding_xml, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'text/xml',
              'Content-Disposition': 'attachment; filename=mva-melding.xml'}

    response = requests.request("POST", url, headers=header, data=payload)
    printing(response)
