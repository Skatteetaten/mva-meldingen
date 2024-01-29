---
icon: "cloud"
title: "Test & Produksjon"
description: "Informasjon om testing og produksjon"
---

[English](https://skatteetaten.github.io/mva-meldingen/omvendt_eng/test/)

## Endringslogg

| Dato       | Hva ble endret?                                                 |
| :--------- | :-------------------------------------------------------------- |
| 2023.01.26 | Opprettet side for test av mva-melding for omvendt avgiftsplikt |

## Krav til testgjennomføring

Systemleverandørene har ansvar for egen testgjennomføring. Det må fokuseres på at validerings- og innsendingstjenestene fungerer som forventet. Implementasjonsguiden må være avgjørende for å få løsningen på plass for systemleverandørene.

Spørsmål angående test og testmiljø kan sendes til Skatteetaten via <a href="https://www.skatteetaten.no/kontakt/skriv/" target="_blank">Skriv til oss - Skatteetaten</a>

## Testmiljø og testdata

Systemleverandørene må ha testmiljøer som kun består av syntetiske data

Oppkobling mot testmiljøet skjer via ID-porten og i forbindelse med test kan Skatteetatens ID-porten-integrasjon benyttes. Det anbefales å bestille egen integrasjon mot ID-porten så tidlig som mulig da dette er en delvis manuell og tidkrevende prosess. Se mer i [implementasjonsguiden kapittel 3. ID-porten integrasjon](https://skatteetaten.github.io/mva-meldingen/documentation/implementasjonsguide/#3-id-porten-integrasjon)

Systemutviklere skal bruke testbrukere fra Tenor Testdatasøk. Dette er syntetisk testbruker som også skal brukes for pålogging i ID-porten og Altinn. Det vil kun være disse testbrukeren som kan benyttes for å få testet. Testbrukere som ligger tilgjengelig på Digdir sine sider vil ikke kunne brukes. [Her finnes en bruksveiledning for Tenor Testdatasøk](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/mvameldingen/test/Bruksveiledning_Tenor.pdf)

Testmiljøet til Skatteetaten vil være tilgjengelig også etter at ny mva-melding for omvendt avgiftsplikt er lansert, så lenge det er behov for det.

## Testplanlegging

I test er det mulig å:

- Validere en mva-melding med meldingskategori "omvendt_avgiftsplikt" - mva-melding for omvendt avgiftsplikt.
- Sende inn en mva-melding for omvendt avgiftsplikt fra regnskapssystemet.
  Etter at mva-melding for omvendt avgiftsplikt er sendt inn fra regnskapssystemet vil virksomheten motta en kvittering i Altinn (https://tt02.altinn.no/ i test).

Man kan også fullføre en innsending i portalen Min merverdiavgift.

## Testplanlegging - Roller

Roller i Altinn for mva-melding for omvendt avgiftsplikt:

- Du kan fylle ut og sende inn mva-melding for omvendt avgiftsplikt med en av disse rollene (Godkjenne):

  - Regnskapsfører med signeringsrettighet
  - Begrenset signeringsrettighet

- Dersom du har en av disse rollene kan du fylle ut mva-melding for omvendt avgiftsplikt, men ikke sende inn (Utfyller)

  - Ansvarlig revisor
  - Regnskapsmedarbeider
  - Regnskapsfører uten signeringsrettighet
  - Revisormedarbeider

## Oppsummering av test og oppstart i produksjon

Systemleverandørene skal etter avsluttet testperiode og i forkant av produksjon oppsummere testen. Oppsummeringen skal vise hva som er testet, samt status etter gjennomført test inkludert oversikt over feil og mangler. Systemleverandørene skal på skatteetatens forespørsel fremlegge dokumentasjon på hvordan integrasjon er
testet.

# Test av applikasjon ved hjelp av Python script

Det er laget et Python script for manuelt å teste en innsending. Mer informasjon og filer finner du her:
[Test av applikasjon ved hjelp av Python script](https://skatteetaten.github.io/mva-meldingen/test_with_python_script/).

## Testmiljø

### Url'er til testmiljøet

| Tjeneste              | Url                                                                                 |
| :-------------------- | :---------------------------------------------------------------------------------- |
| Validering            | https://idporten-api-sbstest.sits.no/api/mva/grensesnittstoette/mva-melding/valider |
| Innsending            | https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/                    |
| Instans API           | https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/instances           |
| ID-porten integrasjon | https://oidc-ver2.difi.no/idporten-oidc-provider/.well-known/openid-configuration   |
| Altinn tokenveksling  | https://platform.tt02.altinn.no/authentication/api/v1/exchange/id-porten            |

## Produksjonsmiljø

Produksjonsmiljøet er funksjonelt likt med testmiljøet.

### Url'er til produksjonsmiljøet

| Tjeneste              | Url                                                                                 |
| :-------------------- | :---------------------------------------------------------------------------------- |
| Validering            | https://idporten.api.skatteetaten.no/api/mva/grensesnittstoette/mva-melding/valider |
| Innsending            | https://skd.apps.altinn.no/skd/mva-melding-innsending-v1/                           |
| Instans API           | https://skd.apps.altinn.no/skd/mva-melding-innsending-v1/instances                  |
| ID-porten integrasjon | https://oidc.difi.no/idporten-oidc-provider/.well-known/openid-configuration        |
| Altinn tokenveksling  | https://platform.altinn.no/authentication/api/v1/exchange/id-porten                 |
