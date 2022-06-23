import requests


def upload(url, konvolutt_xml, token):
    payload = bytearray(konvolutt_xml, 'utf-8')
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/xml',
              'Content-Disposition': 'attachment; filename=konvolutt.xml'}
    response = requests.request("PUT", url, headers=header, data=payload)

    print("status code:", response.status_code)
    print("reason:", response.reason)
    print("headers:", response.headers)
    print("content:", response.content.decode("utf-8"), "\n")
