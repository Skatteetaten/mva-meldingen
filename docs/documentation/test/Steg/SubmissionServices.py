from enum import Enum


class Environment(Enum):
    tt02 = "https://skd.apps.tt02.altinn.no/"


class LoginMethod(Enum):
    idporten = "idporten"


class App(Enum):
    SIT = "skd/mva-melding-innsending-sit"
