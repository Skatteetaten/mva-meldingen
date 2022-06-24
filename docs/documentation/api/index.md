---
icon: "cloud"
title: "API"
description: "Api-beskrivelser"
---

[English](https://skatteetaten.github.io/mva-meldingen/english/api/)

# MVA Melding Validerings og Innsendings API

## Endringslogg

| Dato       | Hva ble endret?                                                                             |
| :--------- | :------------------------------------------------------------------------------------------ |
| 2021.06.17 | Oppdatert dokumentasjon for [tilbakemeldinger](#hent-tilbakemelding).                       |
| 2021.07.05 | Justerte til riktig datatype for opplastning av vedlegg.                                    |
| 2021.08.03 | Endret URL til valideringstjenesten til riktig verdi.                                       |
| 2021.11.04 | Oppdatert URL for valideringstjenesten.                                                     |
| 2021.11.08 | Oppdatert liste over valideringsfeil                                                        |
| 2021.11.11 | Oppdatert feilmeldinger ved utfylling av mva-melding                                        |
| 2021.12.08 | Oppdatert lovlig content type til binaerVedlegg                                             |
| 2022.03.08 | Betalingsinformasjon kan [lastes ned](#tilbakemeldingsfiler) etter fullføring av innsending |
| 2022.06.24 | Endringer i forbindelse med utvidelse av dokumentasjon for andre meldingstyper              |

## Introduksjon

API'ene fungerer for flere typer meldinger i merverdiavgiftsområdet, som mva-meldinger (tidligere RF-0002/0004 ordinær mva-melding og 0005 omvendt avgiftsplikt) og Skattemelding for merverdiavgiftskompensasjon. Når disse meldingene skal sendes til Skatteetaten fra et sluttbrukersystem (SBS) burde disse APIene brukes:

1. Skatteetatens MVA-Melding validerings API
1. Skatteetatens Altinn3 MVA-Melding-Innsending's API

I API-beskrivelsen brukes mva-melding som en samlebetegnelse på de ulike meldingstypene. API'ene beskrives under. 

# Prosess innsending og validering

Innsending av Mva Melding gjøres mot Skatteetatens Altinn3 Instans API for Innsending. Detaljert beskrivelse av Altinn3's Instans-API finnes her
<a href="https://docs.altinn.studio/teknologi/altinnstudio/altinn-api/app-api/instances/" target="_blank">Altinn Studio Instans API</a>. Inngående kjennskap til dette API'et er ikke nødvendig da denne dokumentasjonen dekker behovet for Mva Melding Innsending.

Det anbefales å benytte <a href="https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/swagger/index.html" target="_blank">swagger dokumentasjonen</a> sammen med denne API-beskrivelsen.

I tillegg finnes det kjørende eksempel på innsending som bruker Jupyter Notebook og python under <a href="https://skatteetaten.github.io/mva-meldingen/documentation/test/" target="_blank">Test</a>

Prosessen gjennomføres med en sekvens av kall mot Instans-API´et og beskrives i detalj under sekvensdiagrammet og er som følger:

1. Autentisering
   - Veksle ID-porten token til Altinn-token
2. Validering mot Skatteetaten
3. Utfylling mot Altinn3-App
   - Opprett instans mot Altinn3-App
   - Last opp MvaMeldingInnsending mot Altinn3-App
   - Last opp mva-melding mot Altinn3-App
   - Last opp vedlegg mot Altinn3-App
4. Fullfør utfylling mot Altinn3-App
5. Fullfør innsending mot Altinn3-App
6. Hent tilbakemelding mot Altinn3-App

Instans API'et til Mva Melding Innsending er tilgjengelig på denne URLen:

```
instansApiUrl = "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/instances"
```

I følgende sekvensdiagram vil applikasjonsUrl'en være skjult, så hvis det er skrevet `POST: /intances/` så er det implisitt `POST: instansApiUrl`

![](Mva-Melding-Innsending-Sekvensdiagram.png)

## Autentisering

### Veksle ID-porten token til Altinn-token

For å veksle ID-porten-tokenet må man gjøre følgende kall:

```JSON
GET `https://platform.tt02.altinn.no/authentication/api/v1/exchange/id-porten`
HEADERS:
    "Authorization": "Bearer " + "{IDPortenToken}"
       "content-type": "application/json"
```

og i responsen vil content være et rykende ferskt altinnToken som brukes som Bearer token i de resterende kallene. Tokenet har i dag en varighet på 8 timer. Senere i 2021 vil Altinn3 tilby refresh-tokens slik at en login vil kunne vare i opptil 3 mnd.

## Valider skattemelding

Tjenesten validerer innholdet i en skattemelding og returnerer en respons med eventuelle feil, avvik og advarsler. Tjenesten vil foreta følgende:

1. Kontroll av meldingsformatet.
2. Kontroll av innholdet og sammensetningen av elementene i mva-meldingen.

Skatteetaten forutsetter at valideringstjenesten blir kalt i forkant av innsending av mva-meldingen.
Dette sikrer at mva-meldingen har korrekt format og innhold og øker sannsynligheten for at mva-meldingen
vil bli godkjent ved innsending.

**URL** : `POST https://<env>/api/mva/grensesnittstoette/mva-melding/valider`

Hvor `<env>` er Miljøspesifikk adresse f.eks. `mp-test.sits.no`

**Body** :

- Iht. XSD: <a href="https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd" target="_blank">Skattemeldingformerverdiavgift.v1.0</a>

**Eksempel** : Innsending av XML på ugyldig format

POST <a href="https://mp-test.sits.no/api/mva/grensesnittstoette/mva-melding/valider" target="_blank">https://mp-test.sits.no/api/mva/grensesnittstoette/mva-melding/valider </a>

Header: `Content-Type: application/xml`

Med innhold (http body)som ikke passerer XML-validering basert på <a href="https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd" target="_blank">XSD</a>:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v1.0">

</mvaMeldingDto>
```

### Response

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
                '{"no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v1.0":innsending}' is expected.
            </informasjon>
        </valideringsDetaljer>
    </valideringsfeil>
</valideringsresultat>

```

## Opprett Instans

En instans er et objekt i altinn som følger prosessen og datamodellen definert av en applikasjon. Skatteetaten har en Mva-Melding-Innsendings applikasjon som har en prosess med foreløpig tre steg for innsending. Stegene er utfyllings-, bekreftelses- og tilbakemeldings-steg.

En instans har i tillegg til å være et objekt, et data-objekt definert av en datamodell i appen.

Når en instans er opprettet vil den være mulig å oppdatere data-objektet til instansen og legge til andre data-objekter i appens datamodell. Dette gjøres i neste steg.

For å opprette en instans utfører man en POST mot instansApiUrl med et `instanceOwner`-objekt hvor det fylles inn organisasjonsnummeret for organisasjonen det skal sendes mva melding for:

```JSON
POST {applikasjonsUrl}/instances/
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "content-type": "application/json"
CONTENT/BODY:
    {
        "instanceOwner": {
            "organisationNumber": "{organisasjonsnummer}"
            }
    }
```

Dette kallet vil opprette instansen og returnere

### Response

```JSON
Response HTTPCode: 201 (OK)
Content:
{
    "id": "{partyId}/{instanceGuid}",
    "instanceOwner": {
        "partyId": "{partyId}",
        "organisationNumber": "{organisasjonsnummer}"
    },
    "appId": "skd/{ApplikasjonsNavn}",
    "org": "skd",
    "selfLinks": {
        "apps": "{instansUrl}", // appens instansUrl
        "platform": "{platformUrl}" // altinn3 plattformens url for instansen
    },
    "data": [
        {
            "id": "{dataGuid}", // {dataGuid} kan benyttes i neste steg
            "instanceGuid": "{instanceGuid}",
            "dataType": "no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v1.0",
            "contentType": "application/xml",
            "blobStoragePath": "skd/{ApplikasjonsNavn}/{instanceGuid}/data/{dataGuid}",
            "selfLinks": {
                "apps": "{instanceDataAppUrl}", // {instanceDataAppUrl} kan benyttes i neste steg
                "platform": "{instanceDataPlatformUrl}"
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

Resten av kallene i sekvensen for innsendingen benytter `instansUrl`. Denne kan bli funnet fra responsen ved opprettelsen av instansen. Se i eksempel responsen over. <br>
`instansUrl` kan enten bruke `selflinks.apps` eller ved å utlede fra `instansApiUrl/{partyId}/{instanceGuid}`, hvor `{partyId}` og `{instanceGuid}` kan bli funnet i `id` feltet for den returnerte instansen.

Eksempel på instansUrl: `https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/instances/3949387/abba061g-3abb-4bab-bab8-c9abbaf1ed50/data/28abba46-dea8-4ab7-ba90-433abba906df`

### Feilmeldinger

_Respons 400 - Bad Request:_ <br>
Eksempel verdi

```JSON
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string"
}
```

_Respons 403 - Forbidden:_ <br>
Eksempel verdi

```JSON
{"type":"https://tools.ietf.org/html/rfc7231#section-6.5.3","title":"Forbidden","status":403,"traceId":"00-44eab35cb9ca2049b24de316f380a774-a724e045b09dfc44-00"}
```

Denne feilmeldingen kan en få hvis en prøver å lage en instanse hvor innlogget bruker ikke har rettigheter til organisasjonen definert i request header.
Dette vil da også gjelde hvis innlogget bruker ikke har tilstrekkelig roller for å opprette en instans.

_Respons 404 - Not Found:_ <br>
Eksempel verdi

```JSON
"Cannot lookup party: Failed to lookup party by organisationNumber: 123456789. The exception was: 404 - Not Found - "
```

Denne feilmeldingen kan en få hvis en setter organisasjonsnummeret i request headeren til noe ugyldig.

## Last Opp MvaMeldingInnsending

MvaMeldingInnsending er en datatype for metadata for innsendingen. Objektet man skal fylle ut blir skapt under instansieringen og vil kunne finnes i instans-objektets `data`-liste og har `"dataType": "no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v0.1"`. Siden dette objektet allerede finnes når man skal laste opp MvaMeldingInnsending, benyttes PUT for å oppdatere data-elementet.

Modellen for MvaMeldingInnsending finnes her: <a href="https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd" target="_blank">no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v1.0.xsd</a>

Url til MvaMeldingInnsending har denne oppbygningen:

```
mvaMeldingInnsendingUrl = {instansApiUrl}/{partyId}/{instanceGuid}/data/{dataGuid}
```

hvor `{dataGuid}` er id til data-objektet til instansen.

Det er 2 måter å komme frem til `mvaMeldingInnsendingUrl` og begge benytter instansens data-liste-element som har datatypen `no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v1.0`. Når instansen blir skapt finnes bare ett element i lista.

Fra data-elementet kan man enten:

- flette inn `{dataGuid}` som finnes som verdi i `"id"` i oppbygningen over,
  - eventuelt bruke `{instansApiUrl}/data/{dataGuid}`
- eller bruke `selfLinks.apps` verdien `{instanceDataAppUrl}`, som vist i instans-responsen i forrige steg.
  - `mvaMeldingInnsendingsUrl = {instanceDataAppUrl}`

Man laster opp MvaMeldingInnsending ved å benytte data-apiet til instansen:

```
PUT {mvaMeldingInnsendingsUrl}
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "content-type": "application/xml"
```

```XML
Content:
<?xml version="1.0" encoding="UTF-8"?>
<mvaMeldingInnsending>
    ...
</mvaMeldingInnsending>
```

Eksempel på xml-fil for mvaMeldingInnsending finnes under <a href="https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/test/eksempler/konvolutt" target="_blank">Test</a>.

### Feilmeldinger

_Respons 403 - Forbidden:_ <br>
Hvis innlogget bruker prøver å laste opp fil til instansen, men personen har ikke riktig roller vil en få response kode 403 tilbake.

## Last Opp MvaMelding

Modellen for <a href="../informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd" target="_blank">no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd</a>

Url for opplasting av Mva Melding har denne oppbygningen:

```
{instansUrl}/data?datatype=mvamelding
```

Mva Melding lastes opp på med følgende request mot instansens data-api:

```JSON
POST {instansUrl}/data?datatype=mvamelding
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "content-type": "text/xml"
    "Content-Disposition": "attachment; filename=mvaMelding.xml"
```

```XML
Content:
<?xml version="1.0" encoding="UTF-8"?>
<mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v1.0">
    ...
</mvaMeldingDto>
```

Dette kallet vil laste opp xml-dokumentet til instansen.

### Feilmeldinger

_Respons 403 - Forbidden:_ <br>
Hvis innlogget bruker prøver å laste opp fil til instansen, men personen har ikke riktig roller vil en få response kode 403 tilbake.

## Last Opp Vedlegg

Det er mulig å laste opp fra 0 til 57 vedlegg, med en individuell størrelse på 25MB.

Url for opplasting av Vedlegg har denne oppbygningen:

```
{instansUrl}/data?datatype=binaerVedlegg
```

Det tillates opplasting av følgende content-typer:

- text/xml
- application/pdf
- application/vnd.oasis.opendocument.formula
- application/vnd.oasis.opendocument.text
- application/vnd.oasis.opendocument.spreadsheet
- application/vnd.oasis.opendocument.presentation
- application/vnd.oasis.opendocument.graphics
- application/vnd.openxmlformats-officedocument.wordprocessingml.document
- application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
- application/vnd.openxmlformats-officedocument.presentationml.presentation
- application/msword
- application/vnd.ms-excel
- application/vnd.ms-powerpoint
- image/jpeg
- image/png

Vedlegg lastes opp på med følgende request mot instansens data-api:

```JSON
POST {instansUrl}/data?datatype=binaerVedlegg
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "content-type": "application/pdf"
    "Content-Disposition": "attachment; filename=merknaderTilMvaMeldingen.pdf"
Content:
{pdf-vedlegg i binærformat}
```

Dette kallet vil laste opp pdf-dokumentet til instansen.

Husk at `content-type` skal være passende for vedlegget som skal lastes opp og at filnavnet i `Content-Disposition`- headeren også bør være passende og unikt. Det er dette filnavnet Skatteetaten vil forholde seg til for vedlegget.

### Feilmeldinger

_Respons 403 - Forbidden:_ <br>
Hvis innlogget bruker prøver å laste opp fil til instansen, men personen har ikke riktig roller vil en få response kode 403 tilbake.

## Fullfør utfylling

Dette steget bruker prosess-apiet til instansen og instansen vil avslutte utfyllingssteget for Mva Melding Innsending og til neste steg i applikasjonens prosess for instansen.

For å fullføre utfyllingen utføres følgende kall mot prosess-apiet til instansen:

```JSON
PUT {instansUrl}/process/next
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "content-type": "application/json"
```

Innsendingen vil nå være i bekreftelses-steget.

### Feilmeldinger

_Respons 403 - Forbidden:_ <br>
Hvis innlogget bruker prøver å bytte til neste steg i instansprossessen, men personen har ikke riktig roller vil en få response kode 403 tilbake.

_Respons 409 - Conflict:_ <br>
Eksempel verdi

```JSON
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string"
}
```

```
"Valideringsfeil: Organisasjonsnummeret i instansen er forskjellig fra organisasjonsnummeret i MvaMeldingInnsending (\"konvolutt\")"
```

Hvis organisasjonsnummeret som ble brukt til å lage instansen er forskjellig fra organisasjonsnummeret definert i MvaMeldingInnsending vil en få denne feilmeldingen.

```
"Valideringsfeil: Organisasjonsnummeret i MvaMeldingInnsending (\"konvolutt\") er forskjellig fra organisasjonsnummeret i {filnavn}"
```

Hvis organisasjonsnummeret som er definert i MvaMeldingInnsending er forskjellig fra organisjasnonsnummeret som er definert i mva-meldingen vil en få denne feilmeldingen.

```
"Valideringsfeil: Liste med vedlegg definert i MvaMeldingInnsending (\"konvolutt\") er forskjellig fra listen med vedlegg som er lastet opp i instansen."
```

Hvis listen over vedlegg som er definert i MvaMeldingInnsending er forskjellig fra de som har blitt lastet opp instansen vil en få denne feilmeldingen.

```
"Valideringsfeil: Meldingskategorien i MvaMeldingInnsending (\"konvolutt\") er forsjellig fra Meldingskategorien i {filnavn}"
```

Hvis verdien i meldingskategori feltet for MvaMeldingInnsending er forskjellig fra meldingskategorien i mva-meldigen vil en få denne feilmeldingen.

```
"Valideringsfeil: skattleggingsperiode er påkrevd i MvaMeldingInnsending. Validation error: skattleggingsperiode is required in MvaMeldingInnsending"
```

Hvis verdien i skattleggingsperiode feltet i MvaMeldingInnsending er null vil en få denne feilmeldingen.

```
"Valideringsfeil: skattleggingsperiode må være utfylt. Validation error: skattleggingsperiode must be populated"
```

Hvis verdien i skattleggingsperiode feltet i MvaMeldingInnsending er tom vil en få denne feilmeldingen.

```
"Valideringsfeil: instansstatus er påkrevd i MvaMeldingInnsending. Validation error: instansstatus is required in MvaMeldingInnsending"
```

Hvis verdien i instansstatus feltet i MvaMeldingInnsending er null vil en få denne feilmeldingen.

**Valideringstjenesten**

```
"Valideringsfeil: Ugyldig mva-melding"
```

Appen vil også kalle valideringstjenesten under fullføring av utfyllingen. Hvis mva-meldingen er ugyldig,
vil det returneres feilmelding 409 og valideringsresultatet i xml som content.

Eksempel verdi:

```XML
<valideringsresultat>
    <status>UGYLDIG_SKATTEMELDING</status>
    <valideringsfeil>
        <stiTilFeil>//innsending</stiTilFeil>
        <valideringsDetaljer>
            <feilmelding>Mva meldingen må være på gyldig format og passere XML skjema valideringen</feilmelding>
            <alvorlighetsgrad>UGYLDIG_SKATTEMELDING</alvorlighetsgrad>
            <avvikKode>MvaMeldingsinnhold_Xml_SkjemaValideringsfeil</avvikKode>
            <informasjon>cvc-complex-type.2.4.b: The content of element 'mvaMeldingDto' is not complete. One of
                '{"no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v1.0":innsending}' is expected.
            </informasjon>
        </valideringsDetaljer>
    </valideringsfeil>
</valideringsresultat>
```

For en liste over valideringsfeil, kan man finne under [Valideringsregler](/documentation/forretningsregler/).

**Validering av MvaMeldingInnsending opp mot xsd modellen**
<a href="../informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd" target="_blank">no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd</a>

Eksempel:

```
Valideringsfeil / Validation error:
The 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0:skattleggingsperiodeToMaaneder' element is invalid - The value 'juli-september' is invalid according to its datatype 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0:SkattleggingsperiodeToMaaneder' - The Enumeration constraint failed.
The element 'mvaMeldingInnsending' in namespace 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0' has invalid child element 'opprettingstidspunkt' in namespace 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0'. List of possible elements expected: 'opprettetAv' in namespace 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0'.
```

## Fullfør MvaMeldingInnsending

Dette steget bruker prosess-apiet til instansen og instansen vil avslutte bekreftelsessteget for Mva Melding Innsending og oppdatere instansen til neste steg i applikasjonens prosess.

For å fullføre innsendingen utføres følgende kall mot prosess-apiet til instansen:

```JSON
PUT {instansUrl}/process/next
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "content-type": "application/json"
```

Innsendingen vil nå være i tilbakemeldings-steget.

### Feilmeldinger

_Respons 403 - Forbidden:_ <br>
Hvis innlogget bruker prøver å bytte til neste steg i instansprossessen, men personen har ikke riktig roller vil en få response kode 403 tilbake.

### Betalingsinformasjon tilgjengelig

Når Innsendingen er fullført og instansen nå er i tilbakemeldings-steget, vil betalingsinformasjonen være tilgjengelig på instansen. Den kan finnes ved å hente instansen og laste ned fila `betalingsinformasjon.xml`, og har datatypen `betalingsinformasjon`. Se [tilbakemeldingsfiler](#tilbakemeldingsfiler).

## Hent tilbakemelding

Skatteetaten har laget 2 api-endepunkter for å forenkle utviklingen av dette steget:

- Et endepunkt som returnerer en status for om Skatteetaten har gitt tilbakemelding.
- Et synkront endepunkt som returnerer instansen når Skatteetaten har behandlet mva-meldingen og gitt tilbakemelding.

Det følgende sekvensdiagrammet viser hvordan man kan identifisere om Skatteetaten har gitt tilbakemelding til en gitt instans, og hvordan instansen kan hentes.
![](Hente-Tilbakemelding.png)

For å hente status for tilbamelding kan man utføre kall mot instansens feedback-api:

```JSON
GET {instansUrl}/{partyId}/{instanceGuid}/feedback/status
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "accept": "application/json"
```

Hvis kallet er vellykket vil en få status kode 200 og et json objekt i retur:

```JSON
{
  "isFeedbackProvided":	boolean
}
```

hvor `isFeedbackProvided` returneres som `true` dersom tilbakemelding er gitt, som `false` ellers.

<br>
For å hente en instans hvor tilbakemelding er gitt kan man utføre et kall mot det synkrone API-endepunktet:

```JSON
GET {instansUrl}/{partyId}/{instanceGuid}/feedback
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "accept": "application/json"
```

Dette endepunktet vil returnere instansen når Skatteetaten har gitt tilbakemelding, og vil inneholde data-elementer for alle tilbakemeldingsfilene fra Skatteetaten.

**Merk: Sistnevnte endepunkt skal kun brukes i følgende situasjoner:**

- Sluttbruker venter på tilbakemelding.
- Etter at status-endepunktet har returnert `isFeedbackProvided : true`

### Feilmeldinger

_Respons 400 - Bad Request:_ <br>
Eksempel verdi

```JSON
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string"
}
```

_Respons 403 - Forbidden:_ <br>
Hvis innlogget bruker prøver å hente instansen, men personen har ikke riktig roller vil en få response kode 403 tilbake.

_Respons 404 - Not Found:_ <br>
Eksempel verdi

```JSON
{
  "type": "string",
  "title": "string",
  "status": 0,
  "detail": "string",
  "instance": "string"
}
```

### Tilbakemeldingsfiler

Når Skatteetaten har gitt tilbakemelding, vil filene til tilbakemeldingen kunne lastes ned fra instansen.

Betalingsinformasjonen vil kunne lastes etter [innsendingen er fullført](#fullf%C3%B8r-mvameldinginnsending), da den blir produsert under fullføringen.

Eksempler på tilbakemeldingsfiler som er gitt for en innsending den 17.06.2021 <a href="https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/test/eksempler/feedback/exampleSuccessfulFeedback17062021" target="_blank">finnes her</a>. Disse filene ble lastet ned fra instansen for innsendingen.

Filene som kan lastes ned vil ha `dataType`:

- betalingsinformasjon
- valideringsresultat
- kvittering

og URL'er for nedlastning finnes i instans-objektets `data`-element returnert fra feedback- eller instans-api'et som vist under (irrelevant json er fjernet).

Gitt ett `data` element, kan filen hentes ved å bruke:

```JSON
GET {selfLinks.apps}
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
```

hvor `selfLinks.apps` kan hentes fra listen med data-elementer på instansen som vist her:

```JSON
  "data": [
    {
      "id": "82c96a52-ad0b-428f-8005-7f214daf367e",
      "instanceGuid": "55604b08-1690-4a8d-bf6b-95c11dc40c58",
      "dataType": "valideringsresultat",
      "filename": "valideringsresultat.xml",
      "contentType": "text/xml",
      "selfLinks": {
        "apps": "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-sit/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/82c96a52-ad0b-428f-8005-7f214daf367e",
        "platform": "https://platform.tt02.altinn.no/storage/api/v1/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/82c96a52-ad0b-428f-8005-7f214daf367e"
      }
    },
    {
      "id": "726a315f-7e5e-4514-8ef1-5eda624407d4",
      "instanceGuid": "55604b08-1690-4a8d-bf6b-95c11dc40c58",
      "dataType": "betalingsinformasjon",
      "filename": "betalingsinformasjon.xml",
      "contentType": "text/xml",
      "selfLinks": {
        "apps": "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-sit/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/726a315f-7e5e-4514-8ef1-5eda624407d4",
        "platform": "https://platform.tt02.altinn.no/storage/api/v1/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/726a315f-7e5e-4514-8ef1-5eda624407d4"
      }
    },
    {
      "id": "cbce850a-a887-4598-aea4-710ea9ffdc7d",
      "instanceGuid": "55604b08-1690-4a8d-bf6b-95c11dc40c58",
      "dataType": "kvittering",
      "filename": "kvittering.pdf",
      "contentType": "application/pdf",
      "selfLinks": {
        "apps": "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-sit/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/cbce850a-a887-4598-aea4-710ea9ffdc7d",
        "platform": "https://platform.tt02.altinn.no/storage/api/v1/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/cbce850a-a887-4598-aea4-710ea9ffdc7d"
      }
    }
  ]
```
