import requests


def get(header):
    if header is None:
        print("Something went wrong. header = None")
        return
    url = "https://platform.tt02.altinn.no/authentication/api/v1/exchange/id-porten"
    header["content-type"] = "application/json"
    response = requests.request("GET", url, headers=header)

    print("status code:", response.status_code)
    print("reason:", response.reason)
    print("headers:", response.headers)
    print("content:", response.content.decode("utf-8"), "\n")

    return response.content.decode("utf-8")
