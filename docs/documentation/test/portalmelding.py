from hent import main_relay
import requests

# Slå av sertifikat verifikasjon i test
import urllib3
urllib3.disable_warnings()

PORTAL_MELDING_URL = "https://mp-test.sits.no/api/mva/mva-melding"

def valider_melding(token: dict, xml: str = None) -> None:
    url = f"{PORTAL_MELDING_URL}/valider"
    token["content-type"] = "application/xml"
    r = requests.post(url, data=xml, headers=token, verify=False)
    r.raise_for_status()
    return r


if __name__ == '__main__':
    print("0. Generer ID-porten token.")
    idporten_header = main_relay()
    print('1. kall "valider melding" (bruk ID-porten token fra punkt0 i header-felt "Authorization").')


