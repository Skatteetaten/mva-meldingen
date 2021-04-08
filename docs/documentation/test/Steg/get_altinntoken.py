import requests
from Steg.SubmissionServices import printing, LoginMethod

idporten = LoginMethod.idporten.name
maskinporten = LoginMethod.maskinporten.name


def get(login_method, header):
    if header is None:
        print("Something went wrong. header = None")
        return
    if login_method == idporten:
        url = "https://platform.tt02.altinn.no/authentication/api/v1/exchange/id-porten"
        header["content-type"] = "application/json"
    if login_method == maskinporten:
        url = "http://altinn3local.no/authentication/api/v1/exchange/maskinporten"
    response = requests.request("GET", url, headers=header)
    printing(response)

    return response.content.decode("utf-8")
