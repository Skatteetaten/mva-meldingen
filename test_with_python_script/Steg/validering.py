import requests
import urllib3
from Steg.hent_idporten_token import get_idtoken
from test_with_python_script.config import altinn3_app

# Turn off certificate verification in test.
urllib3.disable_warnings()


def valider_mva_melding(app, token: dict, xml: str = None):
    url = "https://idporten-api-sbstest.sits.no/api/mva/grensesnittstoette/mva-melding/valider"
    if app == altinn3_app.SIT.value:
        url = "https://skatt-utv3.sits.no/api/mva/mva-melding/valider"
    if app == altinn3_app.YT.value:
        url = "https://skatt-yt.sits.no/api/mva/grensesnittstoette/mva-melding/valider"

    token["content-type"] = "application/xml"
    r = requests.post(url, data=xml, headers=token, verify=False)
    print("content:", r.content.decode("utf-8"), "\n")
    return r


def valider_eksempel_fil(app, token: dict, filnavn: str) -> str:
    url = "https://idporten-api-sbstest.sits.no/api/mva/grensesnittstoette/mva-melding/valider"
    if app == altinn3_app.SIT.value:
        url = "https://skatt-utv3.sits.no/api/mva/mva-melding/valider"
    if app == altinn3_app.YT.value:
        url = "https://skatt-yt.sits.no/api/mva/grensesnittstoette/mva-melding/valider"

    token["content-type"] = "application/xml"
    file_path = 'Resources/melding/' + filnavn
    with open(file_path, 'r') as file:
        xml = file.read().replace('\n', '').replace('\t', '').replace('%', '')
        r = requests.post(url, data=xml, headers=token, verify=False)
        r.raise_for_status()
        return r.content.decode('utf-8')


if __name__ == '__main__':
    print("0. Generate ID-porten token.")
    idporten_header = get_idtoken()
    print('1. Call "validate message" (Use ID-porten token from point 0 in the header-field "Authorization"')


