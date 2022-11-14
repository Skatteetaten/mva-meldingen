---
icon: "cloud"
title: "Test & Produksjon"
description: "Informasjon om testing og produksjon"
---

[English](https://skatteetaten.github.io/mva-meldingen/mvameldingen_eng/test/)

## Endringslogg

| Dato       | Hva ble endret?                                                                              |
| :--------- |:---------------------------------------------------------------------------------------------|
| 2022.03.09 | La til miljøinformasjon for [produksjon](#produksjonsmilj%C3%B8) og [test](#testmilj%C3%B8). |
| 2022.03.31 | Rettet en skrivefeil på Altinn instans API for testmiljøet                                   |
| 2022.05.11 | La til ny informasjon om testbrukere fra Tenor                                               |
| 2022.15.11 | Fjernet Jupyter notebook demo og la i stedet inn Phyton script og dokumentasjon på egen side |

## Krav til testgjennomføring

Systemleverandørene har ansvar for egen testgjennomføring. Det må fokuseres på at validerings- og innsendingstjenestene fungerer som forventet. Implementasjonsguiden må være avgjørende for å få løsningen på plass for systemleverandørene.

Prosjektet bistår med feilsøk, evt. feilretting, samt oppfølging av saker som er sendt inn i testmiljøet.

Prosjektet er tilgjengelig via Slack for tekniske avklaringer og direkte kontakt med utviklere og testleder. Prosjektet kan også nås via mva-modernisering@skatteetaten.no. Ta kontakt via mailadressen for å få tilgang til Slack.

## Testmiljø og testdata

Systemleverandørene må ha testmiljøer som kun består av syntetiske data

Oppkobling mot testmiljøet skjer via ID-porten og i forbindelse med test kan Skatteetatens ID-porten-integrasjon benyttes. Det anbefales å bestille egen integrasjon mot ID-porten så tidlig som mulig da dette er en delvis manuell og tidkrevende prosess. Se mer i [implementasjonsguiden kapittel 3. ID-porten integrasjon](https://skatteetaten.github.io/mva-meldingen/documentation/implementasjonsguide/#3-id-porten-integrasjon)

Systemutviklere skal bruke testbrukere fra Tenor Testdatasøk. Dette er syntetisk testbruker som også skal brukes for pålogging i ID-porten og Altinn. Det vil kun være disse testbrukeren som kan benyttes for å få testet. Testbrukere som ligger tilgjengelig på Digdir sine sider vil ikke kunne brukes. [Her finnes en bruksveiledning for Tenor Testdatasøk](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/mvameldingen/test/Bruksveiledning_Tenor.pdf).

Testmiljøet til Skatteetaten vil være tilgjengelig også etter at ny mva-melding er lansert, så lenge det er behov for det.

## Testplanlegging

Prosjektet vil tilby egne møter med fokus på testplanlegging og gjennomføring av test. Her vil tema blant annet være testgjennomføringen, hvilke scenarier som bør testes og testdata.

## Oppsummering av test og oppstart i produksjon

Systemleverandørene skal etter avsluttet testperiode og i forkant av produksjon oppsummere testen. Oppsummeringen skal vise hva som er testet, samt status etter gjennomført test inkludert oversikt over feil og mangler. Systemleverandørene skal på skatteetatens forespørsel fremlegge dokumentasjon på hvordan integrasjon er
testet.

# Test av applikasjon ved hjelp av Phyton script
Det er laget et Phyton script for manuelt å teste en innsending. Mer informasjon og filer finner du her:
[Test av applikasjon ved hjelp av Phyton script](https://skatteetaten.github.io/mva-meldingen/test_with_phyton_script/).

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
