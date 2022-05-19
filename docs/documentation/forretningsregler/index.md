---
icon: "cloud"
title: "Valideringsregler"
description: "Regler for utfylling av mva-melding "
---

### Endringslogg

<table align=center>
  <tr><th style="width:25%" align=left>Dato</th><th align=left> Hva ble endret? </th></tr>
    <tr>
      <td>2022.05.18</td>
      <td>
          <ul>
            <li> R085 sjekk at beløpet på grunnlag er lik eller mindre enn maxverdi i henhold til krav fra DVH</li>
          </ul>      
      </td>
    </tr>
    <tr>
      <td>2022.04.27</td>
      <td>
          <ul>
            <li> R060 forlis unntak lagt til</li>
            <li> R079 KID nummer må oppfylle mod10 eller mod11 validering </li>
            <li> R079 KID nummer kan ikke være lik kontonummeret </li>
            <li> R084 sjekk at det er innsendt spesifikasjonslinjer når fastsatt merverdiavgift har et beløp som er ikke 0 </li>
          </ul>      
      </td>
    </tr>
    <tr>
      <td>2021.12.14</td>
      <td>
          <ul>
            <li> Oppdater avvik tekster for alle regler </li>
            <li> R055 - R058 slettet og R083 lagt til for å erstatte dem </li>
          </ul>      
      </td>
    </tr>
    <tr>
      <td>2021.12.03</td>
      <td>
          <ul>
            <li> R039 tatt bort at 'uttak' spesifikasjon er gyldig på mva kode 32 </li>
            <li> R040 lagt til at 'justering' spesifikasjon er gyldig på mva kode 81 </li>
            <li> R059 og R060 unntak tilfeller skal kun gjelde for påbegynnte skatteleggingsperioder </li>
          </ul>      
      </td>
    </tr>
    <tr>
      <td>2021.11.18</td>
      <td>
          <ul>
            <li> R020 og R021 er nå satt til alvorlighetsgrad "ugyldig skattemelding" </li>
            <li> R022 slettet (dekket av R078) </li>
            <li> R023 - R027 typo korrigert </li>
            <li> R023 - R027 er nå satt til alvorlighetsgrad "avvikende skattemelding" </li>
            <li> R023 - R027 identifisere inngående linjer med sjekk på grunnlag istedenfor merverdiavgift </li>
            <li> R028 - R032 sjekk antall utgående linjer er mer enn antall inngående linjer ikke bare at en utgående linjer finnes </li>
            <li> R059 og R060 unntak for skattepliktig som har meldt konkurs </li>
            <li> R067 og R068 slettet. utgående koder nå validert i R066. R081 lagt til for å validere mva-koder med både inn- og utgående linjer </li>
            <li> R082 sjekk for desimaltall lagt til </li>
          </ul>      
      </td>
  </tr>
  <tr>
      <td>2021.10.29</td>
      <td>
          <ul>
            <li> R001 - R003 og R069 - R071 tekniske regler lagt til </li>
            <li> R000 og R077 praktiske regler lagt til </li>
            <li> R060 og R061 meldinger levert for tidligere terminer regler lagt til </li>
          </ul>      
      </td>
  </tr>
  <tr>
      <td>2021.10.12</td>
      <td>
          <ul>
            <li> Tekst for regel R018 var korrigert. </li>
            <li> R020 - R022 sjekker både merknad felt </li>
            <li> R028 - R032 er nå satt til alvorlighetsgrad "ugyldig skattemelding" </li>
            <li> R028 - R037 korriger sjekk av inn- og utgående linjer </li>
            <li> R047 - R058 skal ikke kjøre hvis register data utilgjengelig, tekst endret </li>
            <li> R072 og R073 lagt til for bedre tilbakemelding hvis en feil oppstår med plikt </li>
            <li> R059 og R060 unntak for skattepliktig som har meldt opphør, konkursbo eller dødsbo </li>
            <li> R066 tekst endring </li>
            <li> R067 og R068 oppdatert å håndtere kode 81 unntak </li>
            <li> R078 lagt til (tilbakeføring spesifikasjon kreves merknad) </li>
            <li> R079 lagt til (KID validering) </li>
            <li> R080 lagt til (Kontonummer oppgitt for utbetalinger) </li>
            <li> R004 - R017 fast merknadsregler erstattet med R074 - R076 som bruker kodeliste merknadTilsvarendeMvaKode </li>
          </ul>      
      </td>
  </tr>
  <tr>
      <td>2021.06.07</td>
      <td>
          <ul>
            <li> Mva-kode 5 lagt til som gjeldende mva-kode for uttak. </li>
            <li> Mva-kode 81 lagt til som gjeldende mva-kode for tilbakeføring av inngående mva. </li>
            <li> Alvorlighetsgrad "mangelfull melding" er fjernet og reglene som brukt det bruker nå alvorlighetsgrad "avvikende skattemelding". </li>
            <li> Reglene R023 - R027 er nå satt til alvorlighetsgrad "ugyldig skattemelding". </li>
            <li> Tekst for regel R040 var korrigert. </li>
          </ul>      
      </td>
  </tr>
  <tr>
      <td>2021.06.28</td>
      <td>
          <ul>
            <li> Valideringsregler R065-R068 lagt til detaljspesifikasjonen. </li>
          </ul>      
      </td>
  </tr>
</table>

## Valideringsregler

Valideringsreglene er under utvikling og nye valideringsregler vil bli lagt til fortløpende.
Følgende valideringsregler er foreløpig definert for mva-meldingen:

- Summen av merverdiavgift for hver avgiftslinje er ikke lik feltet fastsattMerverdiavgift
- Beregnet avgift i avgiftslinje er ulik produktet av grunnlag og sats
- Merknad til beløp med motsatt fortegn som gjelder grunnlag og utgående avgift mangler
- Merknad til beløp med motsatt fortegn som gjelder fradragsført inngående avgift mangler
- Merknad til beløp med motsatt fortegn som gjelder spesifikasjonslinje for tilbakeføring av inngående mva. gitt i mval §9-6 og §9-7
- Fradragsført inngående avgift som gjelder varer kjøpt fra utlandet med fradragsrett, skal være mindre enn eller lik utgående avgift (kode 81)
- Fradragsført inngående avgift som gjelder varer kjøpt fra utlandet med fradragsrett, skal være mindre enn eller lik utgående avgift (kode 83)
- Fradragsført inngående avgift som gjelder tjenester kjøpt fra utlandet med fradragsrett skal være mindre enn eller lik utgående avgift (kode 86)
- Fradragsført inngående avgift som gjelder tjenester kjøpt fra utlandet med fradragsrett skal være mindre enn eller lik utgående avgift (kode 88)
- Fradragsført inngående avgift som gjelder kjøp av klimakvoter og gull med fradragsrett, skal være mindre enn eller lik utgående avgift
- Utgående avgift skal være beregnet dersom det er ført fradrag for inngående avgift som gjelder kjøp av varer fra utlandet med fradragsrett (kode 81)
- Utgående avgift skal være beregnet dersom det er ført fradrag for inngående avgift som gjelder kjøp av varer fra utlandet med fradragsrett (kode 83)
- Utgående avgift skal være beregnet dersom det er ført fradrag for inngående avgift som gjelder tjenester kjøpt fra utlandet med fradragsrett (kode 86)
- Utgående avgift skal være beregnet dersom det er ført fradrag for inngående avgift som gjelder tjenester kjøpt fra utlandet med fradragsrett (kode 88)
- Utgående avgift skal være beregnet dersom det er ført fradrag for inngående avgift som gjelder kjøp av klimakvoter og gull med fradragsrett
- Det skal være fradragsført inngående avgift dersom det er beregnet utgående avgift ved kjøp av varer fra utlandet med fradragsrett (kode 81)
- Det skal være fradragsført inngående avgift dersom det er beregnet utgående avgift ved kjøp av varer fra utlandet med fradragsrett (kode 83)
- Det skal være fradragsført inngående avgift dersom det er beregnet utgående avgift for tjenester kjøpt fra utlandet med fradragsrett (kode 86)
- Det skal være fradragsført inngående avgift dersom det er beregnet utgående avgift for tjenester kjøpt fra utlandet med fradragsrett (kode 88)
- Det skal være fradragsført inngående avgift dersom det er beregnet utgående avgift ved kjøp av klimakvoter og gull med fradragsrett
- Spesifikasjonslinje som gjelder tap på krav kan kun sendes inn på mva-kode 1, 11, 12 eller 13
- Spesifikasjonslinje som gjelder uttak kan kun sendes inn på mva-kode 3, 5, 31 eller 33
- Spesifikasjonslinje som gjelder justering kan kun sendes inn på mva-kode 1 eller 81
- Spesifikasjonslinje som gjelder tilbakeføring av inngående mva. gitt i mva §9-6 og §9-7 kan kun sendes inn på mva-kode 1 eller 81
- Oppgitt meldingskategori skal stemme med opplysningene i mva-registeret (alminnelig)
- Oppgitt meldingskategori skal stemme med opplysningene i mva-registeret (primær)
- Oppgitt skattleggingsperiodetype skal stemme med opplysningene i mva-registeret (alminnelig)
- Oppgitt skattleggingsperiodetype skal stemme med opplysningene i mva-registeret (primær)
- Rapporterende enhet i en fellesregistrering skal ha mva-plikt
- Avgiftspliktig omsetning skal være under en million for alminnelig næring plikter med årlig skattleggingsperiode
- Spesifikasjonslinjer skal ha en gyldig mva-kode i mva-meldinger som gjelder en alminnelig næring plikt
- Spesifikasjonslinjer skal ha en gyldig mva-kode i mva-meldinger som gjelder en primærnæring plikt
- Mva-meldingen skal ikke sendes inn før gjeldende skattleggingsperiode er ferdig (alminnelig)
- Mva-meldingen skal ikke sendes inn før gjeldende skattleggingsperiode er ferdig (primær)
- Mva-meldinger for tidligere terminer skulle vært levert
- Mva-meldinger for tidligere terminer skulle vært levert og derfor vil avgift til gode for denne terminen ikke bli utbetalt
- Inngående mva. skal føres uten grunnlag og sats
- Utgående mva. skal føres med grunnlag og sats
- Spesifikasjonslinje som gjelder tilbakeføring av inngående mva. gitt i mva §9-6 og §9-7 må sendes med en merknad
- Kontonummer må være registrert for meldinger som kunne føre til en utbetaling
- Fradrag for inngående avgift skal normalt ikke føres på en plikt som gjelder engangsregistrering
- Merknader må være gyldig for brukt mva-kode (vanlig fortegn)
- Merknader må være gyldig for brukt mva-kode (motsatt fortegn)
- Merknader må være gyldig for brukt mva-kode (linje med spesifikasjon)

Følgende tekniske regler er også spesifisert som validerer xsd format og kodelister verdier:

- Mva-meldingen skal være på gyldig format
- Spesifikasjonslinjer skal bare bruke kjente mva-koder
- Spesifikasjonslinjer skal bare bruke gyldige satser
- Spesifikasjonslinjer skal bare bruke kjente spesifikasjoner
- Spesifikasjonslinjer skal bare bruke kjente merknader på utvalgt merknad felt
- Mva-meldingen skal bare bruke en kjent merknad på utvalgt merknad felt

To praktiske regler er også definert for å hindre feilaktige innsendinger til det nye systemet:

- Innsending og validering tjeneste er ikke tilgjengelig før 01.01.2022
- Innsending og validering av mva-meldinger fra før 2022 er ikke tilgjengelig

## Detaljspesifikasjon av reglene:

Validering av mva-meldingen er implementert med et sett av regler som kjøres maskinelt
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

```kotlin
    INNLEVERING_FØR_1_1_2022(
        "Innsending og validering av mva-melding er ikke tilgjengelig enda." {
            valideringsregel {
                nå måVæreEtterEllerLik førsteJan2022
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R000 }
        }
    ),
    INNLEVERING_MELDING_FRA_FØR_2022(
        "Det kan ikke sendes inn mva-melding for perioder før 01.01.2022. Denne må sendes via Altinn." {
            valideringsregel {
                skattleggingsperiodeår måVæreEtterEllerLik år2022
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R077 }
        }
    ),
    MVA_MELDINGSINNHOLD_SUM_MVA_FEIL_SUMMERING_AV_AVGIFTLINJER(
        "Summen av merverdiavgift for alle kodelinjene er ikke lik beløpet som er oppgitt som fastsatt merverdiavgift." {
            valideringsregel {
                mvaSpesifikasjonslinje.summenAv { linje ->
                    linje.merverdiavgift
                } skalVære skattegrunnlagOgBeregnetSkatt.fastsattMerverdiavgift
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R018 }
        }
    ),
    MVA_MELDINGSINNHOLD_GRUNNLAG_GANGER_GJELDENDE_SATS_FEIL_BEREGNET_MERVERDIAVGIFT_FOR_AVGIFTSLINJE(
        "Beregnet merverdiavgift i kodelinjen er ikke lik produktet av grunnlag og sats." {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.grunnlag ikkeEr tomt }
                    .skal { linje -> linje.grunnlag * linje.sats væreRundetNedTil linje.merverdiavgift }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R019 }
        }
    ),

    MVA_MELDINGSINNHOLD_UTGÅENDE_MOTSATT_FORTEGN_MERKNAD_TIL_MVA_KODEN_MANGLER(
        "Det må fylles ut merknad som forklarer hvorfor det er benyttet motsatt fortegn for grunnlag og utgående merverdiavgift."
        {
            valideringsregel {
                kodene(3, 6, 31, 32, 33, 51, 52, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92)
                    .hvor { linje -> linje.grunnlag erMindreEnn 0.0 }
                    .skal { linje ->
                        (linje.merknad?.beskrivelse har innhold) eller
                            (linje.merknad?.utvalgtMerknad har innhold)
                    }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R020 }
        }
    ),

    MVA_MELDINGSINNHOLD_INNGÅENDE_MOTSATT_FORTEGN_MERKNAD_TIL_MVA_KODEN_MANGLER(
        "Det må fylles ut merknad som forklarer hvorfor det er benyttet motsatt fortegn for fradragsført merverdiavgift."
        {
            valideringsregel {
                kodene(1, 11, 12, 13, 14, 15, 81, 83, 86, 88, 91)
                    .hvor { linje -> linje.grunnlag er tomt og (linje.merverdiavgift erStørreEnn 0.0) }
                    .skal { linje ->
                        ((linje.merknad?.beskrivelse har innhold) eller (linje.merknad?.utvalgtMerknad har innhold)) medmindre (
                            linje.mvaKode er "1" og (
                                linje.spesifikasjon væreMedI spesifikasjonene(
                                    JUSTERING.spesifikasjon,
                                    TAPPÅKRAV.spesifikasjon,
                                    TILBAKEFØRING.spesifikasjon
                                )
                                )
                                eller (
                                    linje.mvaKode væreMedI mvaKodene(1, 11, 12, 13) og (
                                        linje.spesifikasjon er TAPPÅKRAV.spesifikasjon.kode
                                        )
                                    )
                            )
                    }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R021 }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_MELLOM_BEREGNET_OG_INNGÅENDE_AVGIFT_MVA_KODE_81(
        "Fradrag for innførselsmerverdiavgift skal normalt ikke overstige utgående innførselsmerverdiavgift."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 81 og (linje.grunnlag er tomt) }
                    .såSkal {
                        utgåendeMerverdiavgiftMvaKode(81) uansettFortegnVæreStørreEllerLikEnn inngåendeMerverdiavgiftMvaKode(81)
                    }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R023 }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_MELLOM_BEREGNET_OG_INNGÅENDE_AVGIFT_MVA_KODE_83(
        "Fradrag for innførselsmerverdiavgift skal normalt ikke overstige utgående innførselsmerverdiavgift."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 83 og (linje.grunnlag er tomt) }.såSkal {
                    utgåendeMerverdiavgiftMvaKode(83) uansettFortegnVæreStørreEllerLikEnn inngåendeMerverdiavgiftMvaKode(83)
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R024 }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_MELLOM_BEREGNET_OG_INNGÅENDE_AVGIFT_MVA_KODE_86(
        "Fradrag for inngående merverdiavgift ved kjøp av tjenester fra utlandet skal normalt ikke overstige utgående merverdiavgift for kjøp av tjenester fra utlandet."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 86 og (linje.grunnlag er tomt) }.såSkal {
                    utgåendeMerverdiavgiftMvaKode(86) uansettFortegnVæreStørreEllerLikEnn inngåendeMerverdiavgiftMvaKode(86)
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R025 }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_MELLOM_BEREGNET_OG_INNGÅENDE_AVGIFT_MVA_KODE_88(
        "Fradrag for inngående merverdiavgift ved kjøp av tjenester fra utlandet skal normalt ikke overstige utgående merverdiavgift for kjøp av tjenester fra utlandet."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 88 og (linje.grunnlag er tomt) }.såSkal {
                    utgåendeMerverdiavgiftMvaKode(88) uansettFortegnVæreStørreEllerLikEnn inngåendeMerverdiavgiftMvaKode(88)
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R026 }
        }
    ),

    MVA_MELDINGSINNHOLD_KJØP_AV_KLIMAKVOTER_OG_GULL_MED_FRADRAGSRETT_AVVIK_MELLOM_BEREGNET_OG_INNGÅENDE_AVGIFT_MVA_KODE_91(
        "Fradrag for inngående merverdiavgift ved kjøp av klimakvoter eller gull skal normalt ikke overstige utgående merverdiavgift ved kjøp av klimakvoter eller gull."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 91 og (linje.grunnlag er tomt) }.såSkal {
                    utgåendeMerverdiavgiftMvaKode(91) uansettFortegnVæreStørreEllerLikEnn inngåendeMerverdiavgiftMvaKode(91)
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R027 }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_UTGÅENDE_AVGIFT_MANGLER_MVA_KODE_81(
        "Det skal beregnes utgående innførselsmerverdiavgift i samme termin som fradrag for inngående innførselsmerverdiavgift."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 81 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                    .såSkal {
                        antallUtgåendeLinjerForMvaKode(81) væreStørreEllerLik antallInngåendeLinjerForMvaKode(81)
                    }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R028 }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_UTGÅENDE_AVGIFT_MANGLER_MVA_KODE_83(
        "Det skal beregnes utgående innførselsmerverdiavgift i samme termin som fradrag for inngående innførselsmerverdiavgift."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 83 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                    .såSkal {
                        antallUtgåendeLinjerForMvaKode(83) væreStørreEllerLik antallInngåendeLinjerForMvaKode(83)
                    }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R029 }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_UTGÅENDE_AVGIFT_MANGLER_MVA_KODE_86(
        "Det skal beregnes utgående merverdiavgift ved kjøp av tjenester fra utlandet i samme termin som fradraget gjøres."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 86 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                    .såSkal {
                        antallUtgåendeLinjerForMvaKode(86) væreStørreEllerLik antallInngåendeLinjerForMvaKode(86)
                    }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R030 }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_UTGÅENDE_AVGIFT_MANGLER_MVA_KODE_88(
        "Det skal beregnes utgående merverdiavgift ved kjøp av tjenester fra utlandet i samme termin som fradraget gjøres."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 88 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                    .såSkal {
                        antallUtgåendeLinjerForMvaKode(88) væreStørreEllerLik antallInngåendeLinjerForMvaKode(88)
                    }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R031 }
        }
    ),

    MVA_MELDINGSINNHOLD_KJØP_AV_KLIMAKVOTER_OG_GULL_MED_FRADRAGSRETT_AVVIK_UTGÅENDE_AVGIFT_MANGLER_MVA_KODE_91(
        "Det skal beregnes utgående merverdiavgift ved kjøp av klimakvoter eller gull i samme termin som fradrag for inngående merverdiavgift ved kjøp av klimakvoter eller gull."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er 91 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                    .såSkal {
                        antallUtgåendeLinjerForMvaKode(91) væreStørreEllerLik antallInngåendeLinjerForMvaKode(91)
                    }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R032 }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_INNGÅENDE_AVGIFT_MANGLER_MVA_KODE_81(
        "Ved bruk av koden innførsel av varer med fradragsrett, skal det i samme termin fylles ut fradrag for inngående innførselsmerverdiavgift."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje ->
                    linje.mvaKode er 81 og (linje.grunnlag har innhold) og (linje.spesifikasjon er tomt)
                }.såSkal {
                    mvaSpesifikasjonslinje.inneholder { linje -> linje.mvaKode er 81 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R033 }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_INNGÅENDE_AVGIFT_MANGLER_MVA_KODE_83(
        "Ved bruk av koden innførsel av varer med fradragsrett, skal det i samme termin fylles ut fradrag for inngående innførselsmerverdiavgift."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje ->
                    linje.mvaKode er 83 og (linje.grunnlag har innhold) og (linje.spesifikasjon er tomt)
                }.såSkal {
                    mvaSpesifikasjonslinje.inneholder { linje -> linje.mvaKode er 83 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R034 }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_INNGÅENDE_AVGIFT_MANGLER_MVA_KODE_86(
        "Ved bruk av koden tjenester kjøpt fra utlandet med fradragsrett, skal det i samme termin fylles ut fradrag for inngående merverdiavgift ved kjøp av tjenester fra utlandet."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje ->
                    linje.mvaKode er 86 og (linje.grunnlag har innhold) og (linje.spesifikasjon er tomt)
                }.såSkal {
                    mvaSpesifikasjonslinje.inneholder { linje -> linje.mvaKode er 86 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R035 }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_INNGÅENDE_AVGIFT_MANGLER_MVA_KODE_88(
        "Ved bruk av koden tjenester kjøpt fra utlandet med fradragsrett, skal det i samme termin fylles ut fradrag for inngående merverdiavgift ved kjøp av tjenester fra utlandet."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje ->
                    linje.mvaKode er 88 og (linje.grunnlag har innhold) og (linje.spesifikasjon er tomt)
                }.såSkal {
                    mvaSpesifikasjonslinje.inneholder { linje -> linje.mvaKode er 88 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R036 }
        }
    ),

    MVA_MELDINGSINNHOLD_KJØP_AV_KLIMAKVOTER_OG_GULL_MED_FRADRAGSRETT_AVVIK_INNGÅENDE_AVGIFT_MANGLER_MVA_KODE_91(
        "Ved bruk av koden kjøp av klimakvoter eller gull med fradragsrett, skal det i samme termin fylles ut fradrag for inngående merverdiavgift ved kjøp av klimakvoter eller gull."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje ->
                    linje.mvaKode er 91 og (linje.grunnlag har innhold) og (linje.spesifikasjon er tomt)
                }.såSkal {
                    mvaSpesifikasjonslinje.inneholder { linje -> linje.mvaKode er 91 og (linje.grunnlag er tomt) og (linje.spesifikasjon er tomt) }
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R037 }
        }
    ),

    MVA_MELDINGSINNHOLD_SPESIFIKASJONSLINJE_TAP_PÅ_KRAV_FØRT_PÅ_FEIL_MVA_KODE(
        "Spesifikasjonslinje som gjelder tap på krav kan kun sendes inn på kode 1, 11, 12 eller 13."
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.spesifikasjon er TAPPÅKRAV.spesifikasjon.kode }
                    .skal { linje -> linje.mvaKode væreMedI mvaKodene(1, 11, 12, 13) }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R038 }
        }
    ),

    MVA_MELDINGSINNHOLD_SPESIFIKASJONSLINJE_UTTAK_FØRT_PÅ_FEIL_MVA_KODE(
        "Spesifikasjonslinje som gjelder uttak kan kun sendes inn på kode 3, 5, 31 eller 33."
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.spesifikasjon er UTTAK.spesifikasjon.kode }
                    .skal { linje -> linje.mvaKode væreMedI mvaKodene(3, 5, 31, 33) }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R039 }
        }
    ),

    MVA_MELDINGSINNHOLD_SPESIFIKASJONSLINJE_JUSTERING_FØRT_PÅ_FEIL_MVA_KODE(
        "Spesifikasjonslinje som gjelder justering av merverdiavgift for kapitalvarer kan kun sendes inn på kode 1 og 81."
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.spesifikasjon er JUSTERING.spesifikasjon.kode }
                    .skal { linje -> linje.mvaKode væreMedI mvaKodene(1, 81) }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R040 }
        }
    ),

    MVA_MELDINGSINNHOLD_SPESIFIKASJONSLINJE_TILBAKEFØRING_INNGÅENDE_AVGIFT_9_6_OG_9_7_FØRT_PÅ_FEIL_MVA_KODE(
        "Spesifikasjonslinje som gjelder tilbakeføring av merverdiavgift for kapitalvarer (kun personkjøretøy og fast eiendom), kan kun sendes inn på kode 1 og 81."
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.spesifikasjon er TILBAKEFØRING.spesifikasjon.kode }
                    .skal { linje -> linje.mvaKode væreMedI mvaKodene(1, 81) }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R041 }
        }
    ),

    MVA_PLIKT_OPPGITT_MELDINGSKATEGORI_ALMINNELIG_NÆRING_FINNES_IKKE(
        "Virksomheten er ikke registrert i Merverdiavgiftsregisteret for denne meldingskategorien."
        {
            valideringsregel {
                registerDataHentetOk er OK og (meldingskategori er alminnelig) såSkal {
                    meldingskategori være registrertMeldingskategori
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R047 }
        }
    ),

    MVA_PLIKT_OPPGITT_MELDINGSKATEGORI_PRIMÆRNÆRING_FINNES_IKKE(
        "Virksomheten er ikke registrert i Merverdiavgiftsregisteret for denne meldingskategorien."
        {
            valideringsregel {
                registerDataHentetOk er OK og (meldingskategori er primærnæring) såSkal {
                    meldingskategori være registrertMeldingskategori
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R048 }
        }
    ),

    MVA_PLIKT_OPPGITT_SKATTLEGGINGSPERIODE_FOR__MELDINGSKATEGORI_ALMINNELIG_NÆRING_FINNES_IKKE(
        "Virksomheten er ikke registrert i Merverdiavgiftsregisteret for terminlengden som er oppgitt."
        {
            valideringsregel {
                registerDataHentetOk er OK og
                    (meldingskategori er alminnelig og (registrertSkattleggingsperiodetype har innhold)).såSkal {
                        skattleggingsperiodetype være registrertSkattleggingsperiodetype
                    }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R049 }
        }
    ),

    MVA_PLIKT_OPPGITT_SKATTLEGGINGSPERIODE_FOR__MELDINGSKATEGORI__PRIMÆRNÆRING_FINNES_IKKE(
        "Virksomheten er ikke registrert i Merverdiavgiftsregisteret for terminlengden som er oppgitt."
        {
            valideringsregel {
                registerDataHentetOk er OK og
                    (meldingskategori er primærnæring og (registrertSkattleggingsperiodetype har innhold)) såSkal {
                    skattleggingsperiodetype være registrertSkattleggingsperiodetype
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R050 }
        }
    ),

    MVA_PLIKT_FOR__MELDINGSKATEGORI_DEKKER_IKKE_SKATTELEGGINGSPERIODE_ALMINNELIG(
        "Virksomheten er ikke registrert i Merverdiavgiftsregisteret for skattleggingsperioden som er oppgitt."
        {
            valideringsregel {
                registerDataHentetOk er OK og
                    (meldingskategori er alminnelig og (registrertMeldingskategori er alminnelig)) såSkal {
                    startDatoForPeriodeVæreInnenforGyldigFraOgTilDatoer
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R072 }
        }
    ),

    MVA_PLIKT_FOR__MELDINGSKATEGORI_DEKKER_IKKE_SKATTELEGGINGSPERIODE_PRIMAERNAERING(
        "Virksomheten er ikke registrert i Merverdiavgiftsregisteret for skattleggingsperioden som er oppgitt."
        {
            valideringsregel {
                registerDataHentetOk er OK og
                    (meldingskategori er primærnæring og (registrertMeldingskategori er primærnæring)) såSkal {
                    startDatoForPeriodeVæreInnenforGyldigFraOgTilDatoer
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R073 }
        }
    ),

    MVA_PLIKT_DELTAKERE_I_FELLESREGISTRERING_HAR_IKKE_MVA_PLIKT(
        "Mva-melding for fellesregistrerte virksomheter må sendes inn av rapporterende enhet."
        {
            valideringsregel {
                registerDataHentetOk er OK og (registrertRapporterendeEnhet har innhold) såSkal {
                    skattepliktig være registrertRapporterendeEnhet
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MVA_REGISTER_OPPLYSNINGER }
            regelnummer { R051 }
        }
    ),

    MVA_MELDINGSINNHOLD_OMSETNING_OVER_EN_MILLON_FOR_ÅRSTERMINPLIKT(
        "For å kunne levere mva-melding for alminnelig næring med årstermin må den avgiftspliktige omsetningen være under en million kroner i året."
        {
            valideringsregel {
                meldingskategori er alminnelig og (skattleggingsperiodetype er årlig) såSkal {
                    omsetning væreMindreEnn 1100000.0
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R052 }
        }
    ),

    MVA_MELDINGSINNHOLD_UGYLDIG_MVA_KODE_FOR_OPPGITT_MELDINGSKATEGORI_ALMINNELIG_NÆRING_MED_PLIKT(
        "Den valgte koden kan ikke benyttes ut ifra hvilke plikter virksomheten er registrert med i Merverdiavgiftsregisteret."
        {
            valideringsregel {
                registerDataHentetOk er OK og
                    (meldingskategori er alminnelig og (registrertMeldingskategori har innhold)) såSkal {
                    mvaSpesifikasjonslinje.skal { linje ->
                        linje.mvaKode væreMedI mvaKodene(
                            1,
                            11,
                            12,
                            13,
                            14,
                            15,
                            3,
                            31,
                            32,
                            33,
                            5,
                            51,
                            52,
                            6,
                            81,
                            82,
                            83,
                            84,
                            85,
                            86,
                            87,
                            88,
                            89,
                            91,
                            92
                        )
                    }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R053 }
        }
    ),

    MVA_MELDINGSINNHOLD_UGYLDIG_MVA_KODE_FOR_OPPGITT_MELDINGSKATEGORI_PRIMÆRNÆRING_MED_PLIKT(
        "Den valgte koden kan ikke benyttes ut ifra hvilke plikter virksomheten er registrert med i Merverdiavgiftsregisteret."
        {
            valideringsregel {
                registerDataHentetOk er OK og
                    (meldingskategori er primærnæring og (registrertMeldingskategori har innhold)) såSkal {
                    mvaSpesifikasjonslinje.skal { linje ->
                        linje.mvaKode væreMedI mvaKodene(
                            1,
                            11,
                            12,
                            13,
                            14,
                            15,
                            3,
                            31,
                            32,
                            33,
                            5,
                            51,
                            52,
                            6,
                            81,
                            82,
                            83,
                            84,
                            85,
                            86,
                            87,
                            88,
                            89,
                            91,
                            92
                        )
                    }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R054 }
        }
    ),

    MVA_PLIKT_SKATTLEGGINGSPERIODEN_FOR__MELDINGSKATEGORI_ALMINNELIG_NÆRING_MÅ_VÆRE_FERDIG(
        "Det kan ikke sendes inn mva-melding før terminen har utløpt."
        {
            valideringsregel {
                meldingskategori er alminnelig såSkal {
                    (nå væreEtter skatteleggingsperiodeSluttdato) medmindre
                        (
                            (nå erEtterEllerLik skatteleggingsperiodeStartdato) og
                                (skattepliktigHarMeldtOpphør eller skattepliktigHarRegistrertKonkurs eller skattepliktigErKonkursbo eller skattepliktigErRegistrertSomDødsbo)
                            )
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R059 }
        }
    ),

    MVA_PLIKT_SKATTLEGGINGSPERIODEN_FOR__MELDINGSKATEGORI_PRIMÆRNÆRING_MÅ_VÆRE_FERDIG(
        "Det kan ikke sendes inn mva-melding før terminen har utløpt."
        {
            valideringsregel {
                meldingskategori er primærnæring såSkal {
                    (nå væreEtter skatteleggingsperiodeSluttdato) medmindre
                        (
                            (nå erEtterEllerLik skatteleggingsperiodeStartdato) og
                                (skattemeldingGjelderForlis eller skattepliktigHarMeldtOpphør eller skattepliktigHarRegistrertKonkurs eller skattepliktigErKonkursbo eller skattepliktigErRegistrertSomDødsbo)
                            )
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { PLIKT }
            regelnummer { R060 }
        }
    ),

    MVA_MELDINGSINNHOLD_AVGIFT_Å_BETALE_TIDLIGERE_TERMINER_MANGLER_MVA_MELDING(
        "Det mangler mva-melding for tidligere terminer."
        {
            valideringsregel {
                historiskeFastsettingDataHentetOk er OK og (fastsattmerverdiavgift erStørreEnn 0.0) såSkal {
                    historiskeMeldinger være levert
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { TIDLIGERE_TERMINER }
            regelnummer { R061 }
        }
    ),

    MVA_MELDINGSINNHOLD_AVGIFT_TIL_GODE_TIDLIGERE_TERMINER_MANGLER_MVA_MELDING(
        "Det mangler mva-melding for tidligere terminer. Avgift til gode for denne terminen vil ikke bli utbetalt."
        {
            valideringsregel {
                historiskeFastsettingDataHentetOk er OK og (fastsattmerverdiavgift erMindreEnn 0.0) såSkal {
                    historiskeMeldinger være levert
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { TIDLIGERE_TERMINER }
            regelnummer { R062 }
        }
    ),

    MVA_KODE_FOR_INNGÅENDE_AVGIFT_HAR_FEILAKTIG_GRUNNLAG_OG_SATS(
        "Beløp som gjelder inngående avgift skal ikke ha med grunnlag og sats."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.hvor { linje ->
                    linje.mvaKode væreMedI mvaKodene(1, 11, 12, 13, 14, 15) eller (
                        linje.spesifikasjon væreMedI spesifikasjonene(
                            JUSTERING.spesifikasjon,
                            TAPPÅKRAV.spesifikasjon,
                            TILBAKEFØRING.spesifikasjon
                        ) og (linje.mvaKode er 1)
                        )
                }
                    .skal { linje -> linje.sats være tomt og (linje.grunnlag være tomt) }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R065 }
        }
    ),

    MVA_KODE_FOR_UTGÅENDE_AVGIFT_MANGLER_GRUNNLAG_OG_SATS(
        "Beløp som gjelder utgående avgift skal ha med grunnlag og sats."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.hvor { linje ->
                    linje.mvaKode væreMedI mvaKodene(3, 5, 6, 31, 32, 33, 51, 52, 82, 84, 85, 87, 89, 92) eller (
                        linje.spesifikasjon er UTTAK.spesifikasjon.kode og (
                            linje.mvaKode væreMedI mvaKodene(
                                3,
                                5,
                                31,
                                32,
                                33
                            )
                            )
                        )
                }
                    .skal { linje -> linje.sats ha innhold og (linje.grunnlag ha innhold) }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R066 }
        }
    ),

    MVA_KODE_FOR_INNGÅENDE_ELLER_UTGÅENDE_FEIL_GRUNNLAG_ELLER_SATS(
        "Inngående spesifikasjonslinjer skal være uten grunnlag og sats, mens utgående spesifikasjonslinjer skal være med grunnlag og sats."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.hvor { linje ->
                    linje.mvaKode væreMedI mvaKodene(81, 83, 86, 88, 91)
                }.skal { linje ->
                    ((linje.sats ha innhold) og (linje.grunnlag ha innhold)) eller
                        ((linje.sats være tomt) og (linje.grunnlag være tomt))
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R081 }
        }
    ),

    MVA_MELDINGSINNHOLD_MERKNAD_MANGLER(
        "Det må fylles ut gyldig merknad for denne spesifikasjonslinjen."
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje ->
                        linje.spesifikasjon er TILBAKEFØRING.spesifikasjon.kode
                    }
                    .skal { linje ->
                        (linje.merknad?.beskrivelse ha innhold) eller (linje.merknad?.utvalgtMerknad ha innhold)
                    }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R078 }
        }
    ),

    MVA_MELDINGSINNHOLD_KID_NUMMER_GYLDIG(
        "KID-nummeret må være gyldig."
        {
            valideringsregel {
                (kidNummer har innhold) såSkal {
                    (kidNummer inneholde kunTallEllerKunTallMedBindestrekEtterSisteSiffer) og
                        (kidNummer haLengdeStørreEnn 1) og (kidNummer haLengdeMindreEnn 26) og
                        (kidNummer.oppfyllerMOD10EllerMOD11Validering()) og
                        (kidNummer erIkkeLik registrertKontonummer)
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R079 }
        }
    ),

    MVA_MELDINGSINNHOLD_KONTONUMMER_FINNES_IKKE(
        "Kontonummer mangler for utbetaling av merverdiavgift."
        {
            valideringsregel {
                (skattegrunnlagOgBeregnetSkatt.fastsattMerverdiavgift kunne føreTilEnUtbetaling) såSkal {
                    registrertKontonummer har innhold
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { KONTONUMMER }
            regelnummer { R080 }
        }
    ),

    MVA_MELDINGSINNHOLD_BELØP_INNEHOLDER_DESIMALER(
        "Innsendte beløp skal ikke inneholde desimaler."
        {
            valideringsregel {
                mvaSpesifikasjonslinje.skal { linje ->
                    linje.merverdiavgift.ikkeInneholderDesimaltall() og linje.grunnlag.ikkeInneholderDesimaltall()
                } og fastsattmerverdiavgift.ikkeInneholderDesimaltall()
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R082 }
        }
    ),

    MVA_MELDINGSINNHOLD_PLIKT_FOR_ENGANGSREGISTRERING(
        "Det skal normalt ikke føres fradrag for inngående avgift på en plikt som gjelder engangsregistrering."
        {
            valideringsregel {
                (registerDataHentetOk er OK) og meldingErInnsendtForEnEngangsregistrering såSkal {
                    mvaSpesifikasjonslinje.detIkkeFinner { linje ->
                        linje.mvaKode væreMedI mvaKodene(
                            1,
                            11,
                            12,
                            13,
                            14,
                            15
                        )
                    }
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R083 }
        }
    ),
    
    MVA_MELDINGSINNHOLD_BELØP_I_FASTSATT_MERVERDIAVGIFT_MANGLER_MVA_KODER(
        "Det må sendes inn mva-koder når det er oppgitt beløp i 'fastsatt merverdiavgift'."
        {
            valideringsregel {
                skattegrunnlagOgBeregnetSkatt.fastsattMerverdiavgift.ikkeEr(0.0) såSkal {
                    mvaSpesifikasjonslinje.ikkeVæreEnTomListe()
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R084 }
        }
    ),

    MVA_MELDINGSINNHOLD_GRUNNLAG_OVERSTIGER_MAKS_VERDI(
        "Beløpet på grunnlaget overstiger maks verdi."
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.grunnlag ikkeEr tomt }
                    .skal { linje -> linje.grunnlag væreLikEllerMindreEnn maksGrunnlagVerdi }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R085 }
        }
    ),

    MVA_KODE_MERKNAD_FORTEGN_GYLDIG_VANLIG_FORTEGN(
        "Det må fylles ut gyldig merknad på kode med vanlig fortegn." {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje ->
                        linje.merknad?.utvalgtMerknad har innhold og linje.harVanligFortegn() og
                            (linje.spesifikasjon er tomt)
                    }
                    .skal { linje ->
                        linje.haGyldigMerknadForOppgittMvaKodeOgBeløpOgSpesifikasjon()
                    }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MERKNAD }
            regelnummer { R074 }
        }
    ),

    MVA_KODE_MERKNAD_FORTEGN_GYLDIG_MOTSATT_FORTEGN(
        "Det må fylles ut gyldig merknad på kode med motsatt fortegn." {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje ->
                        linje.merknad?.utvalgtMerknad har innhold og linje.harMotsattFortegn() og
                            (linje.spesifikasjon er tomt)
                    }
                    .skal { linje ->
                        linje.haGyldigMerknadForOppgittMvaKodeOgBeløpOgSpesifikasjon()
                    }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MERKNAD }
            regelnummer { R075 }
        }
    ),

    MVA_KODE_MERKNAD_FORTEGN_GYLDIG_FOR_SPESIFIKASJON(
        "Det må fylles ut gyldig merknad på kode med oppgitt spesifikasjon og fortegn." {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje ->
                        linje.merknad?.utvalgtMerknad har innhold og (linje.spesifikasjon har innhold)
                    }
                    .skal { linje ->
                        linje.haGyldigMerknadForOppgittMvaKodeOgBeløpOgSpesifikasjon()
                    }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MERKNAD }
            regelnummer { R076 }
        }
    ),

    MvaMeldingsinnhold_Xml_SkjemaValideringsfeil(
        "Mva-meldingen må være på gyldig format og passere XML skjema valideringen." {
            valideringsregel { xmlInput skalXmlValideres OK }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R001 }
        }
    ),

    MvaMeldingsinnhold_MvaKode_UkjentMvaKode(
        "Kodelinjene i mva-meldingen må inneholde gyldige koder." {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .skal { linje -> linje.mvaKode væreMedI mvaKodelisten }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R002 }
        }
    ),

    MvaMeldingsinnhold_MvaSats_UkjentSats(
        "Satsene i mva-meldingen må være gyldige." {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.sats har innhold }
                    .skal { linje -> linje.sats væreMedI gyldigSatsForMvaKodeForPerioden(linje.mvaKode) }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R003 }
        }
    ),

    MvaMeldingsinnhold_MvaSpesifikasjoner_UkjentSpesifikasjon(
        "Spesifikasjonslinjene i mva-meldingen skal være gyldige." {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.spesifikasjon har innhold }
                    .skal { linje -> linje.spesifikasjon væreMedI mvaSpesifikasjoner }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R069 }
        }
    ),

    MvaMeldingsinnhold_SpesifikasjonslinjeMerknad_UkjentMerknad(
        "Utvalgte merknader i mva-spesifikasjonslinjer skal være gyldige." {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.merknad?.utvalgtMerknad har innhold }
                    .skal { linje -> linje.merknad?.utvalgtMerknad væreMedI mvaMeldingMerknader }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R070 }
        }
    ),

    MvaMeldingsinnhold_MvaMeldingMerknad_UkjentMerknad(
        "Utvalgte merknader i mva-meldingen skal være gyldige." {
            valideringsregel {
                (meldingUtvalgtMerknad har innhold).såSkal {
                    meldingUtvalgtMerknad væreMedI mvaMeldingMerknader
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R071 }
        }
    )

```
