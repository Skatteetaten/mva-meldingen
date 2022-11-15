---
icon: "cloud"
title: "Test & Produksjon"
description: "Informasjon om testing og produksjon"
---

[English](https://skatteetaten.github.io/mva-meldingen/kompensasjon_eng/test/)

## Endringslogg

| Dato       | Hva ble endret?                                                      |
|:-----------|:---------------------------------------------------------------------|
| 2022.06.11 | Opprettet side for test kompensasjonsmelding                         |
| 2022.15.11 | Fjernet Jupyter notebook demo og la i stedet inn Python script       |
| 2022.15.11 | Informasjon angående test av kompensasjonsmelding etter 15. november |

## Krav til testgjennomføring

Systemleverandørene har ansvar for egen testgjennomføring. Det må fokuseres på at validerings- og innsendingstjenestene fungerer som forventet. Implementasjonsguiden må være avgjørende for å få løsningen på plass for systemleverandørene.

Prosjektet bistår med feilsøk, evt. feilretting, samt oppfølging av saker som er sendt inn i testmiljøet.

Prosjektet er tilgjengelig via Slack for tekniske avklaringer og direkte kontakt med utviklere og testleder. Prosjektet kan også nås via mva-modernisering@skatteetaten.no. Ta kontakt via mailadressen for å få tilgang til Slack.

## Testmiljø og testdata

Systemleverandørene må ha testmiljøer som kun består av syntetiske data

Oppkobling mot testmiljøet skjer via ID-porten og i forbindelse med test kan Skatteetatens ID-porten-integrasjon benyttes. Det anbefales å bestille egen integrasjon mot ID-porten så tidlig som mulig da dette er en delvis manuell og tidkrevende prosess. Se mer i [implementasjonsguiden kapittel 3. ID-porten integrasjon](https://skatteetaten.github.io/mva-meldingen/documentation/implementasjonsguide/#3-id-porten-integrasjon)

Systemutviklere skal bruke testbrukere fra Tenor Testdatasøk. Dette er syntetisk testbruker som også skal brukes for pålogging i ID-porten og Altinn. Det vil kun være disse testbrukeren som kan benyttes for å få testet. Testbrukere som ligger tilgjengelig på Digdir sine sider vil ikke kunne brukes. [Her finnes en bruksveiledning for Tenor Testdatasøk](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/mvameldingen/test/Bruksveiledning_Tenor.pdf)

Testmiljøet til Skatteetaten vil være tilgjengelig også etter at ny kompensasjonsmelding er lansert, så lenge det er behov for det.

## Testplanlegging

Fra 15. november kan dere i test: 

* Validere en mva-melding med meldingskategori "merverdiavgift kompensasjon" - kompensasjonsmelding.
* Sende inn en kompensasjonsmelding fra regnskapssystemet
* Attestere en kompensasjonsmelding i portalen "Min Merverdiavgift" 

Etter at kompensasjonsmeldingen er sendt inn fra regnskapssystemet vil virksomheten som sender inn motta et varsel i Altinn (https://tt02.altinn.no/ i test). 
I varselet er det en lenke til "Min Merverdiavgift". Velg denne lenken og logg på med en bruker som har rollen for å attestere kompensasjonsmeldingen.

## Testplanlegging - Roller
For å legge til rettigheter for attestering, vennligst se
[Brukerveiledning - Gi rettighet til attestering](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/kompensasjon/test/Bruksveiledning_rettighet_til_attestering_i_komp.pdf).

Roller i Altinn for kompensasjonsmelding:

* Du kan fylle ut og sende inn kompensasjonsmeldingen med en av disse rollene (Godkjenne):
    - Regnskapsfører med signeringsrettighet
    - Begrenset signeringsrettighet

* Dersom du har en av disse rollene kan du fylle ut kompensasjonsmeldingen, men ikke sende inn (Utfyller)
  - Ansvarlig revisor
  - Regnskapsmedarbeider 
  - Regnskapsfører uten signeringsrettighet 
  - Revisormedarbeider

* Attestere i portalen "Min Merverdiavgift" (Attestant):
  - Revisorattesterer - MVA Kompensasjon
  - Ansvarlig revisor (NB! Denne rollen fungerer ikke i test foreløpig)

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
