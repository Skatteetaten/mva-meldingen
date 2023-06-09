---
icon: "cloud"
title: "Spørsmål og svar - kompensasjonsmelding"
description: "Spørsmål og svar - kompensasjonsmelding"
---

[English](https://skatteetaten.github.io/mva-meldingen/kompensasjon_eng/faq/)

## Ny kompensasjonsmelding for merverdiavgift

Moderniseringen sørger for forenkling for næringslivet gjennom forbedringer som felles informasjonsstruktur og regelsett for alle typer mva-meldinger; bedre brukeropplevelse og mer fleksibilitet i oppsettet; støttende digital veiledning og mindre feilkilder. Ny kompensasjonsmelding for merverdiavgift lanseres 01.01.23.

### Når kom ny kompensasjonsmelding for merverdiavgift?

Ny kompensasjonsmelding for merverdiavgift ble lansert 01.01.23. Første frist var 11. april 2023. Meldinger og korrigeringer som gjelder for terminer til og med 31. desember 2022 må leveres på gammelt format i Altinn, slik som tidligere.

### Blir det en overgangsperiode fra gammel til ny tjeneste?

For kompensasjonsmelding for merverdiavgift er det ingen overgangsperiode.

### Vil det finnes en «nødløsning» dersom vi får tekniske problemer?

For kompensasjonsmelding for merverdiavgift vil det være mulig å manuelt fylle inn og sende melding direkte i innlogget tjeneste på Skatteetatens hjemmesider.

### Hvem kan fylle ut kompensasjonsmelding for merverdiavgift, og hvem kan sende inn?

Det gjøres ikke endringer i praksis:

Utfylling: Ansvarlig revisor, Regnskapsmedarbeider, Regnskapsfører uten signeringsrettighet eller Revisormedarbeider.

Signering: Begrenset signeringsrettighet eller Regnskapsfører med signeringsrettighet.

Attestering: Ansvarlig revisor eller Revisorattesterer - MVA Kompensasjon.

### Skal leveringen av kompensasjonsmelding for merverdiavgift skje via Altinn eller via Skatteetatens nettside?

Virksomheter og rådgivere oppfordres til å levere kompensasjonsmelding for merverdiavgift direkte fra regnskapssystemet. For de som ikke har regnskapssystem, eller av annen grunn ikke kan levere gjennom regnskapssystem, har Skatteetaten en egen webbasert innlogget tjeneste som kan brukes for levering av kompensasjonsmelding for merverdiavgift. Altinn vil fortsatt brukes for identifisering og informasjonsutveksling.

### Er levering i innlogget tjeneste en permanent løsning som er åpen for alle (hvis man ikke kan eller vil bruke system-system)?

Ja, innlogget tjeneste er en permanent løsning som er åpen for alle.

### Er det laget et utkast visuelt hvordan den nye meldingen skal se ut i regnskapssystemet?

Skatteetaten stiller ikke krav til hvordan meldingen skal se ut i regnskapssystemet. Målet er at brukerne skal føre regnskap som normalt, og at systemet sammenstiller informasjonen fra regnskapet til kompensasjonsmeldingen, slik at brukeren kan sende inn.

Den nye rapporteringen er kodebasert og legge til rette for digital samhandling. Nummererte poster er erstattet av en dynamisk liste av spesifikasjonslinjer. Det er mulig å gi merknader både samlet og per linje.
Kodelisten for den nye kompensasjonsmeldingen er tilgjengelig på Github, under [Informasjonsmodeller, XSD og kodelister.](https://skatteetaten.github.io/mva-meldingen/kompensasjon/informasjonsmodell/#kodelister)

### Kan man vedlegge dokumentasjon som filvedlegg til kompensasjonsmelding for merverdiavgift?

Ja, man kan vedlegge inntil 50 vedlegg per melding, og vedlegg kan være opp til 25 MB per fil.
Vi vil støtte følgende formater:

    - PDF
    - Open Office XML (OOXML)
    - Open Document Format (ODF)
    - JPG eller PNG

### Hvordan autentiserer man seg for innsending av kompensasjonsmelding for merverdiavgift?

Autentisering skjer via ID-porten, med personlig pålogging for system til system og for innlogget tjeneste. Altinn innlogging med brukernavn og passord kan ikke benyttes. Sluttbrukersystemene må tilby et påloggingsvindu til ID-porten for bruker, slik at bruker kan logge på med eID og SBS får tilbake et ID-porten-token som brukes videre mot Skatteetaten og Altinn sine tjenester. For å slippe å logge på mange ganger varer en pålogging i 8 timer.

Vi ønsker å kunne tilby støtte for maskinporten, og ser på de juridiske og praktiske problemstillingene rundt dette, men det kommer senere. I planene som foreligger nå er det ID-porten som er løsningen.

### Vil det foreligge en kodeliste med beskrivelser for de ulike kodene?

Den kan finnes på [Github.](https://skatteetaten.github.io/mva-meldingen/kompensasjon/informasjonsmodell/#kodelister)

### Skal kodene angis med K i kompensasjonsmeldingen?

Nei, kodene skal ikke angis med K i kompensasjonsmeldingen.

Ved levering av kompensasjonsmelding for merverdiavgift fra regnskapssystem eller i innlogget tjeneste, benyttes kun tallkode, uten bokstaven K foran eller bak. Dette er iht. standard kodeliste i dokumentet «Norwegian SAF-T Standard - VAT/Tax codes».

I dokumentet benyttes bokstaven K kun i beskrivelsen av kodene, for at leseren lettere skal kunne se at mva-koden med tilhørende tekst er relevant for kompensasjonsformål.

## Test

### Vil testingen av kompensasjonsmelding for merverdiavgift være åpen for alle?

Informasjon rundt testing er åpent for alle gjennom [Github](https://skatteetaten.github.io/mva-meldingen/kompensasjon/test/).
