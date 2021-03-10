import requests
from Steg.InnsendingServices import printing, InnloggingType

idporten = InnloggingType.idporten.name


def hent(innloggings_metode, header):
    if header is None:
        print("Something went wrong. header = None")
        return
    url = "https://platform.tt02.altinn.no/authentication/api/v1/exchange/id-porten"
    header["content-type"] = "application/json"
    response = requests.request("GET", url, headers=header)
    printing(response)

    return response.content.decode("utf-8")
