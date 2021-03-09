---
icon: "cloud"
title: "API"
description: "Api-beskrivelser"
---

# MVA Melding Validerings og Innsendings API

MVA Meldinger som skal sendes til Skatteetaten fra et sluttbrukersystem (SBS) burde bruke disse APIene:

1. Skatteetatens MVA-Melding-Validering's API
1. Skatteetatens Altinn3 MVA-Melding-Innsending's API

som beskrives under.

## Overordnet prosess for MVA-Melding-Innsending

Den overordnede prosessen for å sende MVA-Melding:

1. Logge inn via ID-porten
1. Validere MVA-Melding mot Skatteetatens valideringstjeneste
   - Autentisering med ID-porten token
1. Veksle ID-porten token med altinn3-token
1. Sende MVA-Melding mot Skatteetatens Altinn3
   - Autentisering med Altinn3 token

## Valider skattemelding

Tjenesten validerer innholdet i en skattemelding og returnerer en respons med eventuelle feil, avvik og advarsler. Tjenesten vil foreta følgende:

1. Kontroll av meldingsformatet.
2. Kontroll av innholdet og sammensetningen av elementene i mva-meldingen.

Skatteetaten forutsetter at valideringstjenesten blir kalt i forkant av innsending av mva-meldingen.
Dette sikrer at mva-meldingen har korrekt format og innhold og øker sannsynligheten for at mva-meldingen
vil bli godkjent ved innsending.

**URL** : `POST https://<env>/api/mva-melding/valider`

Hvor `<env>` er Miljøspesifikk adresse f.eks. `mp-test.sits.no`

**Body** :

- Iht. XSD: [Skattemeldingformerverdiavgift.v0.9](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9.xsd)

**Eksempel** : Innsending av XML på ugyldig format

POST https://mp-test.sits.no/api/mva-melding/skattemeldingformerverdiavgift/valider

Header: `Content-Type: application/xml`

Med innhold (http body)som ikke passerer XML-validering basert på [XSD](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9.xsd)
:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v0.9">

</mvaMeldingDto>
```

**Retur** :

status: 200
Innhold (body)

```xml
<valideringsresultat>
    <status>UGYLDIG_SKATTEMELDING</status>
    <valideringsfeil>
        <stiTilFeil>//innsending</stiTilFeil>
        <valideringsDetaljer>
            <feilmelding>Mva meldingen må være på gyldig format og passere XML skjema valideringen</feilmelding>
            <alvorlighetsgrad>UGYLDIG_SKATTEMELDING</alvorlighetsgrad>
            <avvikKode>MvaMeldingsinnhold_Xml_SkjemaValideringsfeil</avvikKode>
            <informasjon>cvc-complex-type.2.4.b: The content of element 'mvaMeldingDto' is not complete. One of
                '{"no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v0.8":innsending}' is expected.
            </informasjon>
        </valideringsDetaljer>
    </valideringsfeil>
</valideringsresultat>

```

## Prosess Mva Melding Innsending

# Anskaffelse av Altinn Token

Innsending av Mva Melding gjøres mot Skatteetatens Altinn3 Instans API for Innsending. Detaljert beskrivelse av Altinn3's Instans-API finnes her
[Altinn Studio Instans API]("https://docs.altinn.studio/teknologi/altinnstudio/altinn-api/app-api/instances/"). Inngående kjennskap til dette API'et er ikke nødvendig da denne dokumentasjonen dekker behovet for Mva Melding Innsending.

Prosessen gjennomføres med en sekvens av kall mot Instans-API´et og beskrives i detalj under sekvensdiagrammet og er som følger:

1. Opprett Instans
2. Last Opp 1 MvaMeldingInnsending
3. Last Opp 1 MvaMelding
4. Last Opp 0 eller flere Vedlegg
5. Send Inn Mva Melding Innsending

Instans API'et til Mva Melding Innsending er tilgjengelig på en URL for en applikasjon hos altinn og består av

```
instansApiUrl = <applikasjonsUrl>/instances
```

Det vil være en applikasjon for hvert miljø. ApplikasjonsUrl'en for test-miljøet er:

```
applikasjonsUrl = "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2"
```

Hvilket vil gi følgende:

```
instansApiUrl = "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/instances"
```

I følgende sekvensdiagram vil applikasjonsUrl'en være skjult, så hvis det er skrevet `POST: /intances/` så er det implisitt `POST: <applikasjonsUrl>/instances/` (som er instansApiUrl)

![](Mva-Melding-Innsending-Sekvensdiagram.png)

### Opprett Instans

En instans er et objekt i altinn som følger prosessen og datamodellen definert av en applikasjon. Skatteetaten har en Mva-Melding-Innsendings applikasjon har en prosess med foreløpig ett steg for innsending. Steget er et ufyllings-steg.

En instans har i tillegg til å være et objekt, et data-objekt definert av en datamodell i appen.

Når en instans er opprettet vil den være mulig å oppdatere data-objektet til instansen og legge til andre data-objekter i appens datamodell. Dette gjøres i neste steg.

For å opprette en instans utfører man en POST mot instansApiUrl med et `instanceOwner`-objekt hvor det fylles inn organisasjonsnummeret for organisasjonen det skal sendes mva melding for:

```JSON
POST <applikasjonsUrl>/instances/
HEADERS:
    "Authorization": "Bearer " + <altinnToken>
    "content-type": "application/json"
CONTENT/BODY:
    {
        "instanceOwner": {
            "organisationNumber": <organisasjonsnummer>
            }
    }
```

Dette kallet vil opprette instansen og returnere

```JSON
Response HTTPCode: 201 (OK)
Content:
{
    "id": "<partyId>/<instanceGuid>",
    "instanceOwner": {
        "partyId": "<partyId>",
        "organisationNumber": "<organisasjonsnummer>"
    },
    "appId": "skd/<ApplikasjonsNavn>",
    "org": "skd",
    "selfLinks": {
        "apps": "<instansUrl>", // appens instansUrl
        "platform": "<platformUrl>" // altinn3 plattformens url for instansen
    },
    "data": [
        {
            "id": "<dataGuid>", // <dataGuid> kan benyttes i neste steg
            "instanceGuid": "<instanceGuid>",
            "dataType": "no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v0.1",
            "contentType": "application/xml",
            "blobStoragePath": "skd/<ApplikasjonsNavn>/<instanceGuid>/data/<dataGuid>",
            "selfLinks": {
                "apps": "<instanceDataAppUrl>", // <instanceDataAppUrl> kan benyttes i neste steg
                "platform": "<instanceDataPlatformUrl>"
            },
            "size": 273,
            "locked": false,
            "refs": [],
            "isRead": true,
            "created": "2021-03-01T08:15:25.1139057Z",
            "createdBy": "86257",
            "lastChanged": "2021-03-01T08:15:25.1139057Z",
            "lastChangedBy": "86257"
        }
    ]
    // resten av objektet er snippet bort
}

```

Fra responsen kan man finne `instansUrl` fra enten `selflinks.apps`, eller `instansApiUrl/<partyId>/<instanceGuid>`, hvor man kan finne `<partyId>/<instanceGuid>` i verdien til `id` i det returnerte instans-objektet.

Resten av kallene i sekvensen for innsending benytter `instansUrl`.

### Last Opp MvaMeldingInnsending

MvaMeldingInnsending er en datatype for metadata for innsendingen. Objektet man skal fylle ut blir skapt under instansieringen og vil kunne finnes i instans-objektets `data`-liste og har `"dataType": "no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v0.1"`. Siden dette objektet allerede finnes når man skal laste opp MvaMeldingInnsending, benyttes PUT for å oppdatere data-elementet.

Modellen for [no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v0.1.xsd](../informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v0.1.xsd)

Url til MvaMeldingInnsending har denne oppbygningen:

```
mvaMeldingInnsendingUrl = <instansApiUrl>/<partyId>/<instanceGuid>/data/<dataGuid>
```

hvor `<dataGuid>` er id til data-objektet til instansen.

Det er 2 måter å komme frem til `mvaMeldingInnsendingUrl` og begge benytter instansens data-liste-element som har datatypen `no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v0.1`. Når instansen blir skapt finnes bare ett element i lista.

Fra data-elementet kan man enten:

- flette inn `<dataGuid>` som finnes som verdi i `"id"` i oppbygningen over,
- eller bruke `selfLinks.apps` verdien `<instanceDataAppUrl>`, som vist i instans-responsen i forrige steg.
  - `mvaMeldingInnsendingsUrl = <instanceDataAppUrl>`

Man laster opp MvaMeldingInnsending ved å:

```
PUT <mvaMeldingInnsendingsUrl>
HEADERS:
    "Authorization": "Bearer " + <altinnToken>
    "content-type": "text/xml"
```

```XML
Content:
<?xml version="1.0" encoding="UTF-8"?>
<mvaMeldingInnsending>
    ...
</mvaMeldingInnsending>
```

### Last Opp MvaMelding

### Last Opp Vedlegg

### Send Inn Mva Melding Innsending
