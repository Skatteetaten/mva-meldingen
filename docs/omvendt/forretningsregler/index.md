---
icon: "cloud"
title: "Valideringsregler - omvendt avgiftsplikt melding"
description: "Regler for utfylling av omvendt avgiftsplikt melding "
---

[English](https://skatteetaten.github.io/mva-meldingen/omvendt_eng/forretningsregler/)

### Endringslogg

<table align=center>
  <tr><th style="width:25%" align=left>Dato</th><th align=left> Hva ble endret? </th></tr>
    <tr>
      <td>2022.01.26</td>
      <td>Lagt til side for valideringsregler omvendt avgiftsplikt</td>
    </tr>
</table>

## Valideringsregler

Valideringsreglene er under utvikling og nye valideringsregler vil bli lagt til fortløpende.

Følgende valideringsregler er foreløpig definert for alle mva-meldinger:
- Summen av merverdiavgift for hver avgiftslinje er ikke lik feltet fastsattMerverdiavgift (R018)
- Beregnet avgift i avgiftslinje er ulik produktet av grunnlag og sats (R019)
- Meldingen må være en ordinær (aliminnelig eller primærnæring) melding, krav om kompensasjon eller omvendt avgiftsplikt mva-melding (R104)
- Spesifikasjonslinje som gjelder tilbakeføring av inngående mva. gitt i mva §9-6 og §9-7 må sendes med en merknad (R078)
- KID-nummeret må være gyldig (R079)
- Innsendte beløp skal ikke inneholde desimaler (R082)
- Beløp på grunnlag feltet må være under en maks verdi (R085)
- Merknader må være gyldig for brukt mva-kode (vanlig fortegn) (R074)
- Merknader må være gyldig for brukt mva-kode (motsatt fortegn) (R075)
- Merknader må være gyldig for brukt mva-kode (linje med spesifikasjon) (R076)
- Spesifikasjonslinje som gjelder kjøp med kompensasjonsrett må ha med grunnlag og sats (R116)
- Merverdiavgift i kodelinjer skal ha lavere beløp enn grunnlaget (R122)

Følgende valideringsregler er foreløpig definert for omvendt avgiftsplikt mva-meldinger:
- Terminlengde må være 3-månedlig (R106)
- Merknad til beløp med motsatt fortegn som gjelder grunnlag og utgående avgift mangler (R108)
- Spesifikasjonslinjer skal ha en gyldig mva-kode i omvendt avgiftsplikt mva-meldinger (R113)
- Det må sendes inn spesifikasjonslinjer når det er oppgitt beløp i 'fastsatt merverdiavgift' feltet (R107)
- Utgående mva. skal føres med grunnlag og sats (R109)
- Det skal ikke føres beløp både for koden og tilhørende spesifikasjon (R112)
- Spesifikasjonslinje som gjelder tilbakeføring av inngående mva., tap på krav og uttak kan ikke sendes inn på omvendt avgiftsplikt mva-meldinger (R110)
- Spesifikasjonslinje som gjelder kjøp med kompensasjonsrett kan kun sendes inn på mva-kode 86, 88 og 91 (R111)
- Innsendte koder stemmer ikke med beløpet oppgitt i 'fastsatt merverdiavgift' felt (R119)
- 'fastsatt merverdiavgift' beløpet skal ikke være kr 0 (R118)
- Summert grunnlag må være over kr 2 000 (R117)

Følgende tekniske regler er også spesifisert som validerer xsd format og kodelister verdier:

- Mva-meldingen skal være på gyldig format (R001)
- Spesifikasjonslinjer skal bare bruke kjente mva-koder (R002)
- Spesifikasjonslinjer skal bare bruke gyldige satser (R003)
- Spesifikasjonslinjer skal bare bruke kjente spesifikasjoner (R069)
- Spesifikasjonslinjer skal bare bruke kjente merknader på utvalgt merknad felt (R070)
- Mva-meldingen skal bare bruke en kjent merknad på utvalgt merknad felt (R071)

Følgende praktiske regler er også definert for å hindre feilaktige innsendinger til det nye systemet:

- Innsending og validering tjeneste er ikke tilgjengelig før 01.02.2023 for omvendt avgiftsplikt mva-meldinger (R105)
- Innsending og validering av omvendt avgiftsplikt mva-meldinger fra før 2023 er ikke tilgjengelig (R103)


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
    MVA_MELDINGSKATEGORI_UGYLDIG(
        "Innsending og validering av melding for oppgitt meldingskategori er ikke tilgjengelig enda." {
            valideringsregel {
                meldingskategori måVæreEnAv alminnelig_primær_kompensasjon_eller_omvendtAvgiftsplikt
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R104 }
        }
    ),
    MVA_MELDINGSKATEGORI_OMVENDT_AVGIFTSPLIKT_INNLEVERING_FØR_1_2_2023(
        "Innsending og validering av mva-melding for omvendt avgiftsplikt er ikke tilgjengelig enda." {
            valideringsregel {
                meldingskategori er omvendtAvgiftsplikt såSkal {
                    nå væreEtterEllerLik førsteFeb2023
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R105 }
        }
    ),
    MVA_MELDINGSKATEGORI_OMVENDT_AVGIFTSPLIKT_INNLEVERING_MELDING_FRA_FØR_2023(
        "Mva-melding for omvendt avgiftsplikt kan ikke sendes inn for terminer før 01.01.2023. Det må sendes inn via Altinn." {
            valideringsregel {
                meldingskategori er omvendtAvgiftsplikt såSkal {
                    skattleggingsperiodeår måVæreEtterEllerLik år2023
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R103 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_SPESIFIKASJONSLINJE_KJØP_MED_KOMPENSASJONSRETT(
        "Det skal ikke føres beløp både for koden og tilhørende spesifikasjon."
        {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) såSkal {
                    mvaSpesifikasjonslinje.detIkkeFinnesEnKodeBådeMedOgUtenSpesifikasjon()
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R112 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_MELDINGSINNHOLD_UGYLDIG_TERMINKATEGORI(
        "Mva-meldinger for omvendt avgiftsplikt kan kun sendes inn med terminlengde 3-månedlig."
        {
            valideringsregel {
                meldingskategori er omvendtAvgiftsplikt såSkal {
                    skattleggingsperiodetype være treMånedlig
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R106 }
        }
    ),
    MVA_MELDINGSINNHOLD_GRUNNLAG_ER_LAVERE_ENN_BEREGNET_AVGIFT(
        "Beregnet merverdiavgift i kodelinjen har høyere beløp enn oppgitt grunnlag." {
            valideringsregel {
                (
                    (meldingskategori er alminnelig) eller (meldingskategori er primærnæring) eller (meldingskategori er omvendtAvgiftsplikt)
                    ) såSkal {
                    mvaSpesifikasjonslinje
                        .hvor { linje -> linje.grunnlag erStørreEnn 0.0 }
                        .skal { linje -> linje.grunnlag erStørreEnn linje.merverdiavgift }
                }
            }
            alvorlighetsgrad { Avvikstype.UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R122 }
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
    MVA_OMVENDT_AVGIFTSPLIKT_KODER_FINNES_FASTSATT_MERVERDIAVGIFT_KR_0(
        "Innsendte koder stemmer ikke med beløpet oppgitt i 'Fastsatt merverdiavgift'." {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) såSkal {
                    mvaSpesifikasjonslinje
                        .hvor { linje -> (linje.grunnlag ikkeEr tomt) og (fastsattmerverdiavgift er (0.0)) og       (erFørsteMvaMeldingForTerminOmvendtAvgiftsplikt) }
                        .skal { linje -> linje.grunnlag * linje.sats væreRundetNedTil fastsattmerverdiavgift }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R119 }
        }
    ),

    MVA_OMVENDT_AVGIFTSPLIKT_MELDINGSINNHOLD_UTGÅENDE_MOTSATT_FORTEGN_MERKNAD_TIL_MVA_KODEN_MANGLER(
        "Merknad må legges ved som forklaring på hvorfor det er benyttet motsatt fortegn for grunnlag og utgående merverdiavgift."
        {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) såSkal {
                    kodene(86, 87, 88, 89, 91, 92)
                        .hvor { linje -> linje.grunnlag erMindreEnn 0.0 }
                        .skal { linje ->
                            (linje.merknad?.beskrivelse har innhold) eller
                                (linje.merknad?.utvalgtMerknad har innhold)
                        }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R108 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_MELDINGSINNHOLD_UGYLDIG_MVA_KODE_FOR_OPPGITT_MELDINGSKATEGORI(
        "Koden kan ikke brukes i mva-meldingen for omvendt avgiftsplikt."
        {

            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) såSkal {
                    mvaSpesifikasjonslinje.skal { linje ->
                        linje.mvaKode væreMedI mvaKodene(86, 87, 88, 89, 91, 92)
                    }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R113 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_MANGLER_GRUNNLAG_OG_SATS(
        "Beløp som gjelder utgående avgift skal ha med grunnlag og sats."
        {
            valideringsregel {
                meldingskategori er omvendtAvgiftsplikt såSkal {
                    mvaSpesifikasjonslinje.hvor { linje ->
                        linje.mvaKode væreMedI mvaKodene(86, 87, 88, 89, 91, 92)
                    }
                        .skal { linje -> linje.sats ha innhold og (linje.grunnlag ha innhold) }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R109 }
        }
    ),
    MVA_SPESIFIKASJONSLINJEN_KJØP_MED_KOMPENSASJONSRETT_MANGLER_GRUNNLAG_OG_SATS(
        "Beløp som gjelder utgående avgift skal ha med grunnlag og sats."
        {
            valideringsregel {
                (
                    (meldingskategori er alminnelig) eller (meldingskategori er primærnæring) eller (meldingskategori er omvendtAvgiftsplikt)
                    ) såSkal {
                    mvaSpesifikasjonslinje
                        .hvor { linje -> linje.spesifikasjon er KOMPENSASJONSRETT.spesifikasjon.kode }
                        .skal { linje ->
                            (linje.mvaKode væreMedI mvaKodene(81, 83, 86, 88, 91)) og
                                (linje.sats ha innhold) og (linje.grunnlag ha innhold)
                        }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R116 }
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
    MVA_OMVENDT_AVGIFTSPLIKT_MELDINGSINNHOLD_BELØP_I_FASTSATT_MERVERDIAVGIFT_MANGLER_MVA_KODER(
        "Meldingen må inneholde kodelinjer når det er oppgitt et beløp i 'fastsatt merverdiavgift'."
        {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) og
                    skattegrunnlagOgBeregnetSkatt.fastsattMerverdiavgift.ikkeEr(0.0) såSkal {
                    mvaSpesifikasjonslinje.ikkeVæreEnTomListe()
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R107 }
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
    MVA_OMVENDT_AVGIFTSPLIKT_FASTSATT_MERVERDIAVGIFT_KR_0(
        "Det skal ikke sendes inn mva-melding for omvendt avgiftsplikt når beløpet i 'Fastsatt merverdiavgift' er kr 0."
        {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) og erFørsteMvaMeldingForTerminOmvendtAvgiftsplikt såSkal {
                    fastsattmerverdiavgift ikkeVæreLik kr0
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R118 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_SUM_OMSETNING_UNDER_MINSTEBELØP(
        "Summert grunnlag er under minstegrensen på kr 2 000 og skal ikke innberettes." {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) og detFinnesIkkeEnMvaMeldingTidligereIÅretUnderBeløpsgrenseOmvendtAvgiftsplikt såSkal {
                    mvaSpesifikasjonslinje.summenAv { linje ->
                        linje.grunnlag!!
                    }.væreStørreEllerLik(2000) eller mvaSpesifikasjonslinje.summenAv { linje -> linje.grunnlag!! }
                        .væreLikEllerMindreEnn(0.0)
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R117 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_MELDINGSINNHOLD_UGYLDIG_SPESIFIKASJONSLINJE(
        "Spesifikasjonen som er brukt kan ikke brukes i mva-meldingen for omvendt avgiftsplikt."
        {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) såSkal {
                    mvaSpesifikasjonslinje
                        .inneholderIkke { linje ->
                            (linje.spesifikasjon er TILBAKEFØRING.spesifikasjon.kode) eller
                                (linje.spesifikasjon er TAPPÅKRAV.spesifikasjon.kode) eller
                                (linje.spesifikasjon er UTTAK.spesifikasjon.kode)
                        }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R110 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_SPESIFIKASJONSLINJE_KJØP_MED_KOMPENSASJONSRETT_FØRT_PÅ_FEIL_KODE(
        "Spesifikasjonen som gjelder kjøp med kompensasjonsrett kan kun sendes inn på kode 86, 88 og 91."
        {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) såSkal {
                    mvaSpesifikasjonslinje
                        .hvor { linje -> linje.spesifikasjon er KOMPENSASJONSRETT.spesifikasjon.kode }
                        .skal { linje -> linje.mvaKode væreMedI mvaKodene(86, 88, 91) }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R111 }
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
                    .skal { linje -> linje.spesifikasjon væreMedI mvaSpesifikasjonerForMeldingskategori }
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
                    .skal { linje -> linje.merknad?.utvalgtMerknad væreMedI mvaKodeMerknaderForMeldingskategori }
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
                    meldingUtvalgtMerknad væreMedI mvaMeldingMerknaderForMeldingskategori
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R071 }
        }
    )

```
