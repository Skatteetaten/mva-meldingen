import requests
from Steg.SubmissionServices import printing, Environment

local = Environment.local.name


def delete_last_uploaded_attachment(environment, url, attachment, token):
    if environment == local:
        url = url.replace('https', 'http')

    payload = bytearray(attachment, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'text/xml',
              'Content-Disposition': 'attachment; filename=mva-vedlegg.xml'}

    response = requests.request("DELETE", url, headers=header, data=payload)
    printing(response)
