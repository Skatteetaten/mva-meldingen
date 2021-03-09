from docs.documentation.test.testinnsending.Steg.logge_inn_idporten import hent_idtoken
import requests

# Slå av sertifikat verifikasjon i test
import urllib3
urllib3.disable_warnings()

PORTAL_MELDING_URL = "https://mp-test.sits.no/api/mva/mva-melding"


def valider_melding(token: dict, xml: str = None):
    url = f"{PORTAL_MELDING_URL}/valider"
    token["content-type"] = "application/xml"
    r = requests.post(url, data=xml, headers=token, verify=False)
    print(r)
    print("status code:", r.status_code)
    print("reason:", r.reason)
    print("headers:", r.headers, "\n")
    print("content:", r.content.decode("utf-8"), "\n")
    return r


if __name__ == '__main__':
    print("0. Generer ID-porten token.")
    idporten_header = hent_idtoken()
    print('1. kall "valider melding" (bruk ID-porten token fra punkt0 i header-felt "Authorization").')


