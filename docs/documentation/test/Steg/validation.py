from Steg.log_in_idporten import get_idtoken
import requests

# Turn off certificate verification in test.
import urllib3
urllib3.disable_warnings()

PORTAL_MELDING_URL = "https://mp-test.sits.no/api/mva/mva-melding"


def validate_vat_return(token: dict, xml: str = None):
    url = f"{PORTAL_MELDING_URL}/valider"
    token["content-type"] = "application/xml"
    r = requests.post(url, data=xml, headers=token, verify=False)
    print(r)
    print("status code:", r.status_code)
    print("reason:", r.reason)
    print("headers:", r.headers, "\n")
    print("content:", r.content.decode("utf-8"), "\n")
    return r


def validate_example_file(token: dict, filnavn: str) -> str:
    url = f"{PORTAL_MELDING_URL}/valider"
    token["content-type"] = "application/xml"
    file_path = 'eksempler/melding/' + filnavn
    with open(file_path, 'r') as file:
        xml = file.read().replace('\n', '').replace('\t', '').replace('%', '')
        r = requests.post(url, data=xml, headers=token, verify=False)
        r.raise_for_status()
        return r


if __name__ == '__main__':
    print("0. Generate ID-porten token.")
    idporten_header = get_idtoken()
    print('1. Call "validate message" (Use ID-porten token from point 0 in the header-field "Authorization"')


