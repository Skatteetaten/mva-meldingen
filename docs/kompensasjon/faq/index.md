---
icon: "cloud"
title: "Spørsmål og svar - kompensasjonsmelding"
description: "Spørsmål og svar - kompensasjonsmelding"
---

## Ny kompensasjonsmelding for merverdiavgift

Moderniseringen sørger for forenkling for næringslivet gjennom forbedringer som felles informasjonsstruktur og regelsett for alle typer mva-meldinger; bedre brukeropplevelse og mer fleksibilitet i oppsettet; støttende digital veiledning og mindre feilkilder. Ny kompensasjonsmelding for merverdiavgift lanseres 01.01.23.


### Blir det en overgangsperioder fra gammel til ny tjeneste?

For kompensasjonsmelding for merverdiavgift er det ikke planlagt en overgangsperiode.

### Vil det finnes en «nødløsning» dersom vi får tekniske problemer?

For kompensasjonsmelding for merverdiavgift vil det være mulig å manuelt fylle inn og sende melding direkte i innlogget tjeneste på Skatteetatens hjemmesider.

### Hvem kan fylle ut kompensasjonsmelding for merverdiavgift, og hvem kan sende inn?

Det gjøres ikke endringer fra dagens praksis:

Utfylling: Ansvarlig revisor, Regnskapsmedarbeider, Regnskapsfører uten signeringsrettighet eller Revisormedarbeider.

Signering: Begrenset signeringsrettighet eller Regnskapsfører med signeringsrettighet. 

Attestering: Ansvarlig revisor eller Revisorattesterer - MVA Kompensasjon.

### Når trer kompensasjonsmelding for merverdiavgift i kraft?
Fra 1. januar 2023. Første frist vil være 10. april 2023. Meldinger og korrigeringer som gjelder for terminer til og med 31. desember 2022 må leveres på gammelt format i Altinn, slik som tidligere.

### Skal leveringen av kompensasjonsmelding for merverdiavgift skje via Altinn eller via Skatteetatens nettside?

Virksomheter og rådgivere oppfordres til å levere kompensasjonsmelding for merverdiavgift direkte fra regnskapssystemet. Skatteetaten jobber tett med systemleverandører for å tilrettelegge for dette. For de som ikke har regnskapssystem, eller av annen grunn ikke kan levere gjennom regnskapssystem, utvikler Skatteetaten en egen webbasert innlogget tjeneste som kan brukes for levering av kompensasjonsmelding for merverdiavgift. Altinn vil fortsatt brukes for identifisering og informasjonsutveksling.

### Er levering i innlogget tjeneste en permanent løsning som er åpen for alle (hvis man ikke kan eller vil bruke system-system)?

Ja, innlogget tjeneste er en permanent løsning som er åpen for alle.

### Er det laget et utkast visuelt hvordan den nye meldingen skal se ut i regnskapssystemet?

Skatteetaten stiller ikke krav til hvordan meldingen skal se ut i regnskapssystemet. Målet er at brukerne skal føre regnskap som normalt, og at systemet sammenstiller informasjonen fra regnskapet til kompensasjonsmeldingen, slik at brukeren kan sende inn.

Den nye rapporteringen vil være kodebasert og legge til rette for digital samhandling. Dagens nummererte poster erstattes av en dynamisk liste av spesifikasjonslinjer. Det vil bli mulig å gi merknader både samlet og per linje.
Kodelisten for den nye kompensasjonsmeldingen er tilgjengelig på Github, under [Informasjonsmodeller, XSD og kodelister.](https://skatteetaten.github.io/mva-meldingen/kompensasjon/informasjonsmodell/#kodelister)

### Kan man vedlegge dokumentasjon som filvedlegg til kompensasjonsmelding for merverdiavgift?

Ja, man kan vedlegge inntil 50 vedlegg per melding, og vedlegg kan være opp til 25 MB per fil.
Vi vil støtte følgende formater:

    - PDF
    - Open Office XML (OOXML)
    - Open Document Format (ODF)
    - JPG eller PNG

### Hvordan autentiserer man seg for innsending av kompensasjonsmelding for merverdiavgift?

Autentisering vil skje via ID-porten, med personlig pålogging for system til system og for innlogget tjeneste. Dagens Altinn innlogging med brukernavn og passord vil ikke kunne benyttes. Sluttbrukersystemene må tilby et påloggingsvindu til ID-porten for bruker, slik at bruker kan logge på med eID og SBS får tilbake et ID-porten-token som brukes videre mot Skatteetaten og Altinn sine tjenester. For å slippe å logge på mange ganger varer en pålogging i 8 timer.

Vi ønsker å kunne tilby støtte for maskinporten, og ser på de juridiske og praktiske problemstillingene rundt dette, men det kommer senere. I planene som foreligger nå er det ID-porten som er løsningen.

### Vil det foreligge en kodeliste med beskrivelser for de ulike kodene?

Den kan finnes på [Github.](https://skatteetaten.github.io/mva-meldingen/kompensasjon/informasjonsmodell/#kodelister)


## Test

### Vil testingen av kompensasjonsmelding for merverdiavgift være åpen for alle?

Informasjon rundt testing er åpent for alle gjennom [Github](https://skatteetaten.github.io/mva-meldingen/kompensasjon/test/).
Den som er interessert i å delta på test-løpet i samarbeid med Skatteetaten er velkommen til å ta kontakt gjennom mva-modernisering@skatteetaten.no.

