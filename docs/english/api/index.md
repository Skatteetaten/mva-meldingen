---
icon: "cloud"
title: "API"
description: "API descriptions"
---

## Validating vat listing

The service validtes the content of a wat listing and returns a response providing potential errors, deviations and warnings. The service will do the following:

1. Control the format of the message
2. Control the content and composition of the elements in the mva vat listing

Skatteetaten assumes that the validation service is called before sending in the mva vat listing. This will ensure that the mva vat listing has correct format and content and increases the probability for accepting the mva vat listing when sending in.

**URL** : `POST https://<env>/api/mva-melding/valider`

Hwere `<env>` is an environment specific address, i. e. `skatt-at.sits.no

**Body** :

- According to XSD: [Skattemeldingformerverdiavgift.v0.8](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.8.xsd)

**Example** : Sending in XML on incorrect format

POST https://skatt-at.sits.no/api/mva-melding/skattemeldingformerverdiavgift/valider

Header: `Content-Type: application/xml`

With content (http body) not according to XML validation based on [XSD](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.8.xsd)
:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v0.8">

</mvaMeldingDto>
```

**Return** :

Status: 200
Content (body)

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
