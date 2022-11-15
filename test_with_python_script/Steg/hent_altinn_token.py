import requests


def hent(altinn_plattform_miljø, header):
    if header is None:
        print("Something went wrong. header = None")
        return

    url = f"{altinn_plattform_miljø}/authentication/api/v1/exchange/id-porten"
    header["content-type"] = "application/json"

    response = requests.request("GET", url, headers=header).content.decode("utf-8")

    print(response)

    return response
