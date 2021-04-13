import requests
from Steg.SubmissionServices import printing


def delete_last_uploaded_attachment(url, attachment, token):
    payload = bytearray(attachment, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'text/xml',
              'Content-Disposition': 'attachment; filename=mva-vedlegg.xml'}

    response = requests.request("DELETE", url, headers=header, data=payload)
    printing(response)
