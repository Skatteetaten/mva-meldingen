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

Oppkobling mot testmiljøet skjer via IDporten og i forbindelse med test kan Skatteetatens IDporten-integrasjon benyttes. Det anbefales å bestille egen integrasjon mot ID-porten så tidlig som mulig da dette er en delvis manuell og tidkrevende prosess. Se mer i [implementasjonsguiden kapittel 3. ID-porten integrasjon](https://skatteetaten.github.io/mva-meldingen/documentation/implementasjonsguide/#3-id-porten-integrasjon)

Systemleverandørene vil få utdelt syntetiske testbrukere som også finnes i testmiljøene til IDporten (ver2) og Altinn (TT02).

Testmiljøet til Skatteetaten vil være tilgjengelig i avtalte perioder fra mai og frem til januar 2022. I juli 2021 kan det ikke forventes at miljøet skal være tilgjengelig.

## Testplanlegging

Prosjektet vil tilby egne møter med fokus på testplanlegging og gjennomføring av test. Her vil tema blant annet være testgjennomføringen, hvilke scenarier som bør testes og testdata.

## Oppsummering av test og oppstart i produksjon

Systemleverandørene skal etter avsluttet testperiode og i forkant av produksjon oppsummere testen. Oppsummeringen skal vise hva som er testet, samt status etter gjennomført test inkludert oversikt over feil og mangler. Systemleverandørene skal på skatteetatens forespørsel fremlegge dokumentasjon på hvordan integrasjon er
testet.

## 'Test 4'

I løpet av uke 19 vil all dokumentasjon være oppdatert og tilgjengelig her på github.

Testmiljøet vil være tilgjengelig fra 25.mai.

![Testplan](Testplan.png)
