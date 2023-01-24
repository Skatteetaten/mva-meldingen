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
      <td>2023.01.01</td>
      <td>
          <ul>
            <li> Informasjon om forretningsregler for krav om kompensasjon lagt til </li>
          </ul>      
      </td>
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

Følgende valideringsregler er foreløpig definert for krav om kompensasjon mva-meldinger:

- Mva-meldingen kan ikke sendes inn før terminen har utløpt (R089)
- Terminlengde må være 2-månedlig (R095)
- Merknad til beløp med motsatt fortegn som gjelder fradragsført inngående avgift mangler (R086)
- Spesifikasjonslinjer skal ha en gyldig mva-kode i krav om kompensasjon mva-meldinger (R088)
- Kodelinjer skal føres med grunnlag og sats (R093)
- Det må sendes inn spesifikasjonslinjer når det er oppgitt beløp i 'fastsatt merverdiavgift' feltet (R100)
- Virksomheter som er registrert som et kommunalt foretak kan ikke sende inn mva-meldingen (R094)
- Mva-meldingen må sendes inn før innleveringsfristen for terminen (R096)
- Endring av krav om kompensasjon innsendt etter innleveringsfristen kan ikke være mer til gode enn det som allerede er sendt inn (R097)
- Første krav om kompensasjon for terminen kan ikke være 0 kroner (R098)
- Første krav om kompensasjon til utbetalig for året må være på minst 20 000 kroner (R099)
- Koder 81 og 83 kan kun brukes av registrerte virksomheter (R101)
- Spesifikasjonslinje som gjelder justering kan kun sendes inn på mva-kode 1, 14 eller 81 (R087)
- Spesifikasjonslinje som gjelder tap på krav, uttak eller tilbakeføring av inngående mva. er ugyldig (R091)

Følgende tekniske regler er også spesifisert som validerer xsd format og kodelister verdier:

- Mva-meldingen skal være på gyldig format (R001)
- Spesifikasjonslinjer skal bare bruke kjente mva-koder (R002)
- Spesifikasjonslinjer skal bare bruke gyldige satser (R003)
- Spesifikasjonslinjer skal bare bruke kjente spesifikasjoner (R069)
- Spesifikasjonslinjer skal bare bruke kjente merknader på utvalgt merknad felt (R070)
- Mva-meldingen skal bare bruke en kjent merknad på utvalgt merknad felt (R071)

Følgende praktiske regler er også definert for å hindre feilaktige innsendinger til det nye systemet:

- Innsending og validering tjeneste er ikke tilgjengelig før 01.01.2023 for krav om kompensasjon mva-meldinger (R090)
- Innsending og validering av krav om kompensasjon mva-meldinger fra før 2023 er ikke tilgjengelig (R092)

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
    MVA_KOMPENSASJON_INNLEVERING_FØR_1_1_2023(
        "Innsending og validering av krav om kompensasjon er ikke tilgjengelig enda." {
            valideringsregel {
                meldingskategori er kompensasjon såSkal {
                    nå væreEtterEllerLik førsteJan2023
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R090 }
        }
    ),
    MVA_KOMPENSASJON_INNLEVERING_MELDING_FRA_FØR_2023(
        "Krav om kompensasjon kan ikke sendes inn for terminer før 01.01.2023. Det må sendes inn via Altinn." {
            valideringsregel {
                meldingskategori er kompensasjon såSkal {
                    skattleggingsperiodeår måVæreEtterEllerLik år2023
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R092 }
        }
    ),
    MVA_KOMPENSASJON_SKATTLEGGINGSPERIODEN_FOR__MELDINGSKATEGORI_KOMPENSASJON_MÅ_VÆRE_FERDIG(
        "Krav om kompensasjon kan ikke sendes inn før terminen har utløpt."
        {
            valideringsregel {
                meldingskategori er kompensasjon såSkal {
                    (nå væreEtter skatteleggingsperiodeSluttdato)
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R089 }
        }
    ),
    MVA_KOMPENSASJON_MELDINGSINNHOLD_UGYLDIG_TERMINKATEGORI(
        "Kompensasjonsmelding kan kun sendes inn med terminlengde 2-månedlig."
        {
            valideringsregel {
                meldingskategori er kompensasjon såSkal {
                    skattleggingsperiodetype være toMånedlig
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R095 }
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
    MVA_KOMPENSASJON_MELDINGSINNHOLD_INNGÅENDE_MOTSATT_FORTEGN_MERKNAD_TIL_MVA_KODEN_MANGLER(
        "Merknad må legges ved som forklaring på hvorfor det er benyttet motsatt fortegn."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) såSkal {
                    kodene(1, 11, 13, 14, 15, 81, 83, 86, 88, 91)
                        .hvor { linje -> linje.merverdiavgift erStørreEnn 0.0 }
                        .skal { linje ->
                            ((linje.merknad?.beskrivelse har innhold) eller (linje.merknad?.utvalgtMerknad har innhold)) medmindre (
                                (
                                    linje.mvaKode væreMedI mvaKodene(
                                        1,
                                        14,
                                        81
                                    ) og (linje.spesifikasjon er JUSTERING_KOMPENSASJON.spesifikasjon.kode)
                                    )
                                )
                        }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R086 }
        }
    ),
    MVA_KOMPENSASJON_MELDINGSINNHOLD_UGYLDIG_MVA_KODE_FOR_OPPGITT_MELDINGSKATEGORI(
        "Koden kan ikke brukes i kompensasjonsmelding for merverdiavgift."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) såSkal {
                    mvaSpesifikasjonslinje.skal { linje ->
                        linje.mvaKode væreMedI mvaKodene(1, 11, 13, 14, 15, 81, 83, 86, 88, 91)
                    }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R088 }
        }
    ),
    MVA_KOMPENSASJON_KODE_INNGÅENDE_AVGIFT_MANGLER_GRUNNLAG_OG_SATS(
        "Kodelinjen må ha grunnlag og sats."
        {
            valideringsregel {
                meldingskategori er kompensasjon såSkal {
                    mvaSpesifikasjonslinje.skal { linje ->
                        (linje.sats ha innhold) og (linje.grunnlag ha innhold)
                    }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R093 }
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

    MVA_KOMPENSASJON_MELDINGSINNHOLD_BELØP_I_FASTSATT_MERVERDIAVGIFT_MANGLER_MVA_KODER(
        "Kompensasjonsmeldingen må inneholde kodelinjer når det er oppgitt beløp i 'fastsatt merverdiavgift'."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) og
                    skattegrunnlagOgBeregnetSkatt.fastsattMerverdiavgift.ikkeEr(0.0) såSkal {
                    mvaSpesifikasjonslinje.ikkeVæreEnTomListe()
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R100 }
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
    MVA_KOMPENSASJON_ORG_FORM_KF(
        "Virksomheter som er registrert som et kommunalt foretak kan ikke selv sende inn krav om kompensasjon, dette må gjøres av kommunen."
        {
            valideringsregel {
                meldingskategori er kompensasjon såSkal {
                    virksomhetIkkeVæreKommunaltForetak
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R094 }
        }
    ),
    MVA_KOMPENSASJON_LEVERT_ETTER_INNLEVERINGSFRIST(
        "Krav om kompensasjon er sendt inn etter innleveringsfristen for terminen."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) og erFørsteKompensasjonsmeldingForTermin såSkal {
                    nå væreFørEllerLik innleveringsfrist
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R096 }
        }
    ),
    MVA_KOMPENSASJON_ENDRING_LEVERT_ETTER_INNLEVERINGSFRIST(
        "Endring av krav om kompensasjon sendt inn etter innleveringsfristen for terminen, kan ikke være mer til gode enn det som allerede er sendt inn."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) og erIkkeFørsteKompensasjonsmeldingForTermin såSkal {
                    (nå væreFørEllerLik innleveringsfrist) eller (fastsattmerverdiavgift væreStørreEllerLik tidligereFastsattBeløpForTermin)
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R097 }
        }
    ),
    MVA_KOMPENSASJON_MELDINGSINNHOLD_BELØP_I_FASTSATT_MERVERDIAVGIFT_IKKE_VÆRE_NULL(
        "Første krav om kompensasjon for terminen kan ikke være 0 kroner."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) og erFørsteKompensasjonsmeldingForTermin såSkal {
                    fastsattmerverdiavgift ikkeVæreLik kr0
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R098 }
        }
    ),
    MVA_KOMPENSASJON_MELDINGSINNHOLD_KRAV_UNDER_MINSTEBELØP(
        "Første krav om kompensasjon til utbetaling for året må være på minst 20 000 kroner."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) og
                    detFinnesIkkeEnKompensasjonsmeldingTidligereIÅretOver20000krTilgode såSkal {
                    fastsattmerverdiavgift væreLikEllerMindreEnn -20000.0
                }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R099 }
        }
    ),
    MVA_KOMPENSASJON_MELDINGSINNHOLD_UGYLDIG_MVA_KODE_BRUKT_FOR_IMPORT(
        "Virksomheten er ikke registrert i Merverdiavgiftsregisteret, og kan ikke bruke koder for innførselsmerverdiavgift innberettet på mva-meldingen. Kodene 14 eller 15 må brukes."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) og virksomhetenErIkkeRegistrertMedEnPliktForPerioden såSkal {
                    mvaSpesifikasjonslinje.detIkkeFinner { linje -> (linje.mvaKode er 81) eller (linje.mvaKode er 83) }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R101 }
        }
    ),
    MVA_KOMPENSASJON_MELDINGSINNHOLD_SPESIFIKASJONSLINJE_JUSTERING_FØRT_PÅ_FEIL_MVA_KODE(
        "Spesifikasjon som gjelder justering av krav om kompensasjon på fast eiendom kan kun sendes inn på kode 1, 14 og 81."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) såSkal {
                    mvaSpesifikasjonslinje
                        .hvor { linje -> linje.spesifikasjon er JUSTERING_KOMPENSASJON.spesifikasjon.kode }
                        .skal { linje -> linje.mvaKode væreMedI mvaKodene(1, 14, 81) }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { XSD_FORMAT_OG_LOVLIGE_VERDIER }
            regelnummer { R087 }
        }
    ),
    MVA_KOMPENSASJON_MELDINGSINNHOLD_UGYLDIG_SPESIFIKASJONSLINJE(
        "Spesifikasjonen som er brukt kan ikke brukes i kompensasjonsmelding for merverdiavgift."
        {
            valideringsregel {
                (meldingskategori er kompensasjon) såSkal {
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
            regelnummer { R091 }
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
