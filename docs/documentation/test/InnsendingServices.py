from enum import Enum


class Miljo(Enum):
    tt02 = "https://skd.apps.tt02.altinn.no/"
    local = "http://altinn3local.no/"


class InnloggingType(Enum):
    idporten = "idporten"
    maskinporten = "maskinporten"


class App(Enum):
    SIT = "skd/hack-innsending-mva-melding"
    ETM2 = "skd/mva-melding-innsending-etm2"


def printing(response):
    print(response)
    print("status code:", response.status_code)
    print("reason:", response.reason)
    print("headers:", response.headers, "\n")
    print("content:", response.content.decode("utf-8"), "\n")
