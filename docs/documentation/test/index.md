---
icon: "cloud"
title: "Test"
description: "Testcaser mva-melding og test plan"
---

## Krav til testgjennomføring

Systemleverandørene har ansvar for egen testgjennomføring. Det må fokuseres på at validerings- og innsendingstjenestene fungerer som forventet. Implementasjonsguiden må være avgjørende for å få løsningen på plass for systemleverandørene.

Prosjektet bistår med feilsøk, evt. feilretting, samt oppfølging av saker som er sendt inn i testmiljøet.

Prosjektet er tilgjengelig via Slack for tekniske avklaringer og direkte kontakt med utviklere og testleder. Prosjektet kan også nås via mva-modernisering@skatteetaten.no. Ta kontakt via mailadressen for å få tilgang til Slack.

## Testmiljø og testdata

Systemleverandørene må ha testmiljøer som kun består av syntetiske data

Oppkobling mot testmiljøet skjer via ID-porten og i forbindelse med test kan Skatteetatens ID-porten-integrasjon benyttes. Det anbefales å bestille egen integrasjon mot ID-porten så tidlig som mulig da dette er en delvis manuell og tidkrevende prosess. Se mer i [implementasjonsguiden kapittel 3. ID-porten integrasjon](https://skatteetaten.github.io/mva-meldingen/documentation/implementasjonsguide/#3-id-porten-integrasjon)

Systemleverandørene må ved oppstart av test ta kontakt med prosjektet på MVA-Modernisering@skatteetaten.no for å få tildelt testbruker. Dette er syntetisk testbruker som også skal brukes for pålogging i ID-porten og Altinn. Det vil kun være disse testbrukeren som kan benyttes for å få testet. Testbrukere som ligger tilgjengelig på Digdir sine sider vil ikke kunne brukes.

Testmiljøet til Skatteetaten vil være tilgjengelig i avtalte perioder fra mai og frem til januar 2022. I juli 2021 kan det ikke forventes at miljøet skal være tilgjengelig.

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

## 'Test 4'

I løpet av uke 19 vil all dokumentasjon være oppdatert og tilgjengelig her på github.

Testmiljøet vil være tilgjengelig fra 25.mai.

![Testplan](Testplan.png)
