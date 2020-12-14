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

- Iht. XSD: [Skattemeldingformerverdiavgift.v0.9](https://github.com/Skatteetaten/mva-meldingen/blob/oppdatere-regler-og-api-beskrivelse/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9.xsd)

**Eksempel** : Innsending av XML på ugyldig format

POST https://skatt-at.sits.no/api/mva-melding/skattemeldingformerverdiavgift/valider

Header: `Content-Type: application/xml`

Med innhold (http body)som ikke passerer XML-validering basert på [Melding XSD](https://github.com/Skatteetaten/mva-meldingen/blob/oppdatere-regler-og-api-beskrivelse/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9.xsd)
Eksempel:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v0.9">
</mvaMeldingDto>
```

**Retur** :

status: 200
Innhold (body)

Innholdet er XML i henhold til [Valideringsresultat XSD](https://github.com/Skatteetaten/mva-meldingen/blob/oppdatere-regler-og-api-beskrivelse/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.valideringsresultat.v0.1_%C3%A6%C3%B8%C3%A5.xsd)
:
Eksempel:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<valideringsresultat xmlns="no:skatteetaten:fastsetting:avgift:mva:valideringsresultat:v0.1">
    <avvikVedMeldingslevering>ugyldig skattemelding</avvikVedMeldingslevering>
    <avvik>
        <stiTilAvvik>//mvaMeldingDto</stiTilAvvik>
        <mvaKode>null</mvaKode>
        <avviksinformasjon>
            <begrunnelse>Mva meldingen må være på gyldig format og passere XML skjema valideringen</begrunnelse>
            <avvikstype>ugyldig skattemelding</avvikstype>
            <avvikKode>MvaMeldingsinnhold_Xml_SkjemaValideringsfeil</avvikKode>
            <detaljer>Cannot find the declaration of element 'mvaMeldingDto'.</detaljer>
        </avviksinformasjon>
    </avvik>
</valideringsresultat>

```
