---
icon: "cloud"
title: "Test & Produksjon"
description: "Informasjon om testing og produksjon"
---

## Endringslogg

| Dato       | Hva ble endret?                                                                              |
| :--------- | :------------------------------------------------------------------------------------------- |
| 2022.06.11 | Opprettet side for test kompensasjonsmelding                                                 |

## Krav til testgjennomføring

Systemleverandørene har ansvar for egen testgjennomføring. Det må fokuseres på at validerings- og innsendingstjenestene fungerer som forventet. Implementasjonsguiden må være avgjørende for å få løsningen på plass for systemleverandørene.

Prosjektet bistår med feilsøk, evt. feilretting, samt oppfølging av saker som er sendt inn i testmiljøet.

Prosjektet er tilgjengelig via Slack for tekniske avklaringer og direkte kontakt med utviklere og testleder. Prosjektet kan også nås via mva-modernisering@skatteetaten.no. Ta kontakt via mailadressen for å få tilgang til Slack.

## Testmiljø og testdata

Systemleverandørene må ha testmiljøer som kun består av syntetiske data

Oppkobling mot testmiljøet skjer via ID-porten og i forbindelse med test kan Skatteetatens ID-porten-integrasjon benyttes. Det anbefales å bestille egen integrasjon mot ID-porten så tidlig som mulig da dette er en delvis manuell og tidkrevende prosess. Se mer i [implementasjonsguiden kapittel 3. ID-porten integrasjon](https://skatteetaten.github.io/mva-meldingen/documentation/implementasjonsguide/#3-id-porten-integrasjon)

Systemutviklere skal bruke testbrukere fra Tenor Testdatasøk. Dette er syntetisk testbruker som også skal brukes for pålogging i ID-porten og Altinn. Det vil kun være disse testbrukeren som kan benyttes for å få testet. Testbrukere som ligger tilgjengelig på Digdir sine sider vil ikke kunne brukes. [Her finnes en bruksveiledning for Tenor Testdatasøk](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/mvameldingen/test/Bruksveiledning_Tenor.pdf)

Testmiljøet til Skatteetaten vil være tilgjengelig også etter at ny mva-melding er lansert, så lenge det er behov for det.

## Testplanlegging

Prosjektet vil tilby egne møter med fokus på testplanlegging og gjennomføring av test. Her vil tema blant annet være testgjennomføringen, hvilke scenarier som bør testes og testdata.

## Oppsummering av test og oppstart i produksjon

Systemleverandørene skal etter avsluttet testperiode og i forkant av produksjon oppsummere testen. Oppsummeringen skal vise hva som er testet, samt status etter gjennomført test inkludert oversikt over feil og mangler. Systemleverandørene skal på skatteetatens forespørsel fremlegge dokumentasjon på hvordan integrasjon er
testet.

## Testapplikasjon

Det er skrevet en testapplikasjon som kan brukes i forbindelse med test av løsningen mot Skatteetaten. Den er skrevet i [jupyter notebook formatet](https://jupyter.org/):

1. [Jupyter notebook demo for henting og validering](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/demo.ipynb). Last ned katalogen 'test' og kjør skriptet demo.ipynb (skriptet vil utføre alle trinn som inngår i prosessen: kalle ping tjeneste å sjekke kobling og validere mva-melding)

2. [Jupyter notebook demo for henting, validering og innsending](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/innsending-eksempel.ipynb). Kjør skriptet innsending.ipynb. Den vil kjøre alle stegene i prosessen.

3. [Pyton skript å hent token](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/Steg/log_in_idporten.py) og [postman skript å validere melding](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/MeldingValidering.postman_collection.json). Første logge inn hos [ID-Porten](https://skatteetaten.github.io/mva-meldingen/documentation/idportenautentisering/), og da lagre token i format "Bearer <em>hentet-token</em>" som miljø variabel med navn "test-bearer" i postman, og bruk postman skript å validere melding.

4. [Eksempel XML-er](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/test/eksempler/melding)

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
