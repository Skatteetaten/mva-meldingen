---
icon: "cloud"
title: "Valideringsregler - kompensasjonsmelding"
description: "Regler for utfylling av kompensasjonsmeldingmelding "
---

[English](https://skatteetaten.github.io/mva-meldingen/kompensasjon_eng/forretningsregler/)

### Endringslogg

<table align=center>
  <tr><th style="width:25%" align=left>Dato</th><th align=left> Hva ble endret? </th></tr>
    <tr>
      <td>2022.06.26</td>
      <td>Lagt til side for valideringsregler kompensasjonsmelding</td>
    </tr>
    <tr>
</table>

## Valideringsregler

Valideringsreglene er under utvikling og nye valideringsregler vil bli lagt til fortløpende.
Følgende valideringsregler er foreløpig definert for kompensasjonsmelding for merverdiavgift:

- Summen av merverdiavgift for hver avgiftslinje er ikke lik feltet fastsattMerverdiavgift
- Beregnet avgift i avgiftslinje er ulik produktet av grunnlag og sats
- Merknad til beløp med motsatt fortegn som gjelder kompensasjon av inngående avgift mangler
- Kompensasjonsmeldingen skal ikke sendes inn før gjeldende skattleggingsperiode er ferdig
- Kompensasjon av inngående avgift skal føres med grunnlag og sats
- Kontonummer må være registrert for meldinger som kunne føre til en utbetaling
- Merknader må være gyldig for brukt mva-kode (vanlig fortegn)
- Merknader må være gyldig for brukt mva-kode (motsatt fortegn)
- Kompensasjonsmelding kan kun sendes inn for gyldig terminkategori (2-månedlig)
- Første kompensasjonsmelding for et kalenderår må være på mer enn 20 000 kroner i mva
- Kompensasjonsmelding sendt inn før leveringsfrist må ha revisorattestasjon
- Kompensasjonsmelding kan ikke sendes inn etter leveringsfrist hvis ikke har en godkjent melding eller fastsetting fra Skatteetaten for terminen
- Kompensasjonsmelding sendt inn etter leveringsfrist må ha et lavere tilgodebeløp enn forrige innsendte melding eller fastsetting fra Skatteetaten

Følgende tekniske regler er også spesifisert som validerer xsd format og kodelister verdier:

- Kompensasjonsmeldingen skal være på gyldig format
- Spesifikasjonslinjer skal bare bruke kjente mva-koder
- Spesifikasjonslinjer skal bare bruke gyldige satser
- Spesifikasjonslinjer skal bare bruke kjente spesifikasjoner
- Spesifikasjonslinjer skal bare bruke kjente merknader på utvalgt merknad felt
- Kompensasjonsmeldingen skal bare bruke en kjent merknad på utvalgt merknad felt

To praktiske regler er også definert for å hindre feilaktige innsendinger til det nye systemet:

- Innsending og valideringstjenesten er ikke tilgjengelig før 1.1.2023
- Innsending og validering av kompensasjonsmelding fra før 2023 er ikke tilgjengelig

## Detaljspesifikasjon av reglene - under arbeid:

Validering av kompensasjonsmelding for merverdiavgift er implementert med et sett av regler som kjøres maskinelt
for å sjekke gyldigheten av meldingen.
Reglene er utformet slik at de både er dokumentasjon av reglene for meldingen og kjørbare maskinelt.
Eksempel på regel:

```kotlin {.line-numbers}
[1]     MvaMeldingsinnhold_GrunnlagGangerGjeldendeSats_FeilBeregnetMerverdiavgiftForAvgiftslinje(
[2]        "Beregnet avgift i avgiftslinje er ulik produktet av grunnlag og sats" {
[3]            valideringsregel {
[4]                mvaSpesifikasjonslinje
[5]                    .hvor { linje -> linje.grunnlag ikkeEr tomt }
[6]                    .skal { linje -> linje.grunnlag * linje.sats væreRundetNedTil linje.merverdiavgift }
[7]            }
[8]            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
[9]        }
[10]    )
```

Her betyr feltene i regelen ovenfor følgende:

**Linje 1 - Identifikator**: Dette er referansen til regelen hver regel har en unik identifikator.

**Linje 2 - Feilmelding**: Dette er feilmeldingen som bli returnert i validerings-APIet dersom
MVA-meldingen ikke er i henhold til kravet i regelen.

**Linje 3-7 - Valideringsregel**: Dette er regelen som definerer hvordan en gyldig MVA-melding skal være.
Dersom denne regelen ikke er oppfylt vil meldingsvalideringen feile.

**Linje 8 - Alvorlighetsgrad**: Dette er alvorlighetsgraden dersom valideringen feiler.
Følgende alvorlighetsgrader er definert : AVVIKENDE_SKATTEMELDING, UGYLDIG_SKATTEMELDING


Detaljspesifikasjon for hver enkelt regel vil bli lagt til etterhvert som kompensasjonsmeldingen blir utviklet.
