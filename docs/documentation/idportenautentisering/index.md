---
icon: "cloud"
title: "ID-Porten & Autentisering"
description: "Hvordan autentisere med ID-Porten"
---

## Ta i bruk ID-porten

Når man starter å teste kan Skatteetatens ID-porten-integrasjon benyttes, men det anbefales å bestille egen integrasjon mot ID-porten så tidlig som mulig, både fordi når produksjonssetting intreffer må egen integrasjon mot ID-porten benyttes, og fordi prosessen er delvis manuell. Prosessen går mot Digitaliseringsdirektoratet (DigDir), og detaljer rundt hvordan man oppretter integrasjonen og tar i bruk ID-porten er beskrevet her: https://samarbeid.digdir.no/id-porten/id-porten/18. En annen fordel med å starte prosessen tidlig er at man kan teste integrasjonen i test-miljøet. Det må også opprettes egen integrasjon i produksjon. Under bestillingen må dere oppgi at dere ønsker tilgang til skattemeldings-API fra skatteetaten.

Kundeforholdet hos DigDir gir tilgang til deres selvbetjeningsløsning som igjen gir tilgang til administrasjon av Kundens bruk av ID-porten. I selvbetjeningsløsningen kan kunden opprette en såkalt client_id og definere en callback-url:

- client_id: en unik automatisk generert identifikator for tjenesten.
- callback-url: Uri-en som klienten får lov å redirigere nettleseren til etter innlogging. Etter en vellykket innlogging i ID-porten vil brukeren redirigeres til denne url-en.

Inntil kundeforhold hos DigDir er etablert og integrasjon opprettet, kan sluttbrukersystemene i benytte Skatteetatens integrasjon. For denne testen har Skatteetaten opprettet følgende `client_id` som kan benyttes av sluttbrukersystemene:

- `client_id: 23cc2587-ea4e-4a5f-aa5c-dfce3d6c5f09`
- Callback-URL til denne `client_id` er satt til http://localhost:12345/token (Hvis det er konsumenter som ønsker andre callback-URL kan vi ordne det)

**Nyttige lenker:**

- Klienten bruker test-miljøet i DigDir, "verifikasjon 2": https://samarbeid.difi.no/node/232
- OIDC-integrasjonen er beskrevet her: https://difi.github.io/felleslosninger/oidc_index.html
- Hvordan lage en klient i selvregistreringen: https://minside-samarbeid.difi.no/organization-home/services/service-admin#/

## Logge inn hos ID-porten

ID-porten login kan implementeres i alle typer sluttbrukersystemer

- Desktop Applikasjon
- Web Applikasjon

under forutsetning av at applikasjonen kan åpne en URL i en nettleser hvor login gjennomføres og samtidig som den kan kjøre en web-server som mottar en web-request (i form av en redirect fra ID-porten etter login) på callback-url'en.

Sluttbrukersystemet må gjøre følgende:

- Starte system browser og gjøre autorisasjonskall mot ID-porten. Les mer om det her: https://difi.github.io/felleslosninger/oidc_protocol_authorize.html
- Brukeren blir da sendt til ID-porten for innlogging. Dere kan benytte eksisterende test-brukere som dere benytter til test mot skattemeldingen i dag.
- Sette opp en webserver som venter på callback fra browseren. Etter vellykket pålogging i ID-porten sendes brukes til denne webserveren. Denne webserveren må være satt til å lytte på callback-URL http://localhost:12345/token (ref. forrige kapittel).
- Gjøre et tokenforespørsel. Les mer om det her: https://difi.github.io/felleslosninger/oidc_protocol_token.html

Vi benytter følgende testmiljø hos ID-porten:

- /authorize endpoint: https://oidc-ver2.difi.no/idporten-oidc-provider/authorize
- /token endpoint: https://oidc-ver2.difi.no/idporten-oidc-provider/token

For detaljer rundt hvilken HTTP parametere som må sendes med i kallet, se filen [log_in_idporten.py](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/Steg/log_in_idporten.py)
