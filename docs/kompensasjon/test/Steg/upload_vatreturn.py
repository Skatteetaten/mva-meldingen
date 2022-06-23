import requests


def upload(url, melding_xml, token):
    payload = bytearray(melding_xml, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'text/xml',
              'Content-Disposition': 'attachment; filename=mva-melding.xml'}
    response = requests.request("POST", url, headers=header, data=payload)

    print("status code:", response.status_code)
    print("reason:", response.reason)
    print("headers:", response.headers)
    print("content:", response.content.decode("utf-8"), "\n")
