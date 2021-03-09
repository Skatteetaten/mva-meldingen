import requests
from docs.documentation.test.testinnsending.InnsendingServices import printing, InnloggingType

idporten = InnloggingType.idporten.name
maskinporten = InnloggingType.maskinporten.name


def hent(innloggings_metode, header):
    if header is None:
        print("Something went wrong. header = None")
        return
    if innloggings_metode == idporten:
        url = "https://platform.tt02.altinn.no/authentication/api/v1/exchange/id-porten"
        header["content-type"] = "application/json"
    if innloggings_metode == maskinporten:
        url = "http://altinn3local.no/authentication/api/v1/exchange/maskinporten"
    response = requests.request("GET", url, headers=header)
    printing(response)

    return response.content.decode("utf-8")
