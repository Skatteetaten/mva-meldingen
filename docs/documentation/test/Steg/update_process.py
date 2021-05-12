import requests


def next_step(url, token):
    url = url + "/process/next"
    header = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}
    response = requests.request("PUT", url, headers=header)

    print("status code:", response.status_code)
    print("reason:", response.reason)
    print("headers:", response.headers)
    print("content:", response.content.decode("utf-8"), "\n")

    return response
