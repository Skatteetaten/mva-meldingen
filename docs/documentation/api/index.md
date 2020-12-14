---
icon: "cloud"
title: "API"
description: "Api-beskrivelser"
---

## Valider skattemelding

Tjenesten validerer innholdet i en skattemelding og returnerer en respons med eventuelle feil, avvik og advarsler. Tjenesten vil foreta følgende:

1. Kontroll av meldingsformatet.
2. Kontroll av innholdet og sammensetningen av elementene i mva-meldingen.

Skatteetaten forutsetter at valideringstjenesten blir kalt i forkant av innsending av mva-meldingen.
Dette sikrer at mva-meldingen har korrekt format og innhold og øker sannsynligheten for at mva-meldingen
vil bli godkjent ved innsending.

**URL** : `POST https://<env>/api/mva-melding/valider`

Hvor `<env>` er Miljøspesifikk adresse f.eks. `skatt-at.sits.no

**Body** :

- Iht. XSD: [Skattemeldingformerverdiavgift.v0.8](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.8.xsd)

**Eksempel** : Innsending av XML på ugyldig format

POST https://skatt-at.sits.no/api/mva-melding/skattemeldingformerverdiavgift/valider

Header: `Content-Type: application/xml`

Med innhold (http body)som ikke passerer XML-validering basert på [XSD](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.8.xsd)
:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v0.8">
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
