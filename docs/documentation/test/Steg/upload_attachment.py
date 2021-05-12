import requests


def upload(url, attachment, content_type, token):
    with open("./eksempler/vedlegg/" + attachment, 'rb') as file:
        payload = file.read()
    header = {'Authorization': 'Bearer ' + token, 'content-type': content_type,
              'Content-Disposition': 'attachment; filename=' + attachment}
    response = requests.request("POST", url, headers=header, data=payload)

    print("status code:", response.status_code)
    print("reason:", response.reason)
    print("headers:", response.headers)
    print("content:", response.content.decode("utf-8"), "\n")

    return response
