from enum import Enum


class Environment(Enum):
    tt02 = "https://skd.apps.tt02.altinn.no/"


class LoginMethod(Enum):
    idporten = "idporten"


class App(Enum):
    ETM2 = "skd/mva-melding-innsending-etm2"


def printing(response):
    print(response)
    print("status code:", response.status_code)
    print("reason:", response.reason)
    print("headers:", response.headers, "\n")
    print("content:", response.content.decode("utf-8"), "\n")
