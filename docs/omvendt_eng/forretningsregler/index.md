---
icon: "cloud"
title: "Validation rules"
description: "Validation rules for the VAT tax return"
---

[Norwegian](https://skatteetaten.github.io/mva-meldingen/kompensasjon/forretningsregler/)

### Change log

<table align=center>
	<tr><th style="width:25%" align=left>Date</th><th align=left> What was changed? </th></tr>
<tr>
      <td>2022.06.30</td>
      <td>
          <ul>
            <li> Added page for validation rules for tax return for VAT compensation</li>
          </ul>      
      </td>
    </tr>
    <tr>
      <td>2023.01.01</td>
      <td>
          <ul>
            <li> Added information on validation rules for tax return for VAT compensation</li>
          </ul>      
      </td>
    </tr>
</table>

## Validation rules

The validation rules are under development an new validation rules will be added.

The following validation rules are defined for all VAT returns:

- The sum of the calculated VAT from each VAT line shall be equal to the total VAT in the VAT return (R018)
- The calculated VAT must be in accordance with the stated VAT-basis multiplied by the current VAT-rate (R019)
- The tax return must be an ordinary (general or primary industry) VAT return, claim for compensation or reverse tax liability VAT return (R104)
- Specification lines that apply to the reversal of input VAT given in VAT §9-6 and §9-7 require a remark (R078)
- KID numbers must be valid (R079)
- Values must not contain decimals (R082)
- Values in the basis field must be under a maximum value (R085)
- Remarks must be valid for the given VAT code (expected VAT direction) (R074)
- Remarks must be valid for the given VAT code (opposite VAT direction) (R075)
- Remarks must be valid for the given VAT code (lines with a specification) (R076)

The following validation rules are defined for claim for compensation VAT returns:

- VAT returns must not be sent in before the related tax period has ended (R089)
- The tax periode length must be 2 months (R095)
- Additional information is required to explain why opposite prefixes are used (R086)
- Specification lines must have valid VAT codes (R088)
- Specification lines must be declared with a VAT-basis and VAT-rate (R093)
- The VAT return must contain code lines when an amount has been specified in the 'fastsatt merverdiavgift' field (R100)
- Businesses registered as municipal undertakings cannot submit claims for compensastion (R094)
- Claims for compensation must be sent in before the deadline for the tax period (R096)
- Changes to claims for compensation sent in after the deadline for the tax period can not increase the amount for repayment (R097)
- The first claim for compensation for a tax period cannot be 0 krone (R098)
- The first claim for compensation for the year must be at least a 20 000 krone repayment (R099)
- VAT codes 81 and 83 can only be used by businesses registered in the VAT register (R101)
- Specification lines that apply to the reversal of input VAT given in VAT §9-6 and §9-7 can only be submitted on VAT code 1, 14 or 81 (R087)
- Specification lines that apply to losses on outstanding claims, withdrawals or reversal of input VAT are not valid (R091)

The following technical rules are defined for the purpose of validating the format and code lists in the tax return:

- The VAT return should be in a valid format (R001)
- The specification lines should only use valid VAT codes (R002)
- The specification lines should only use valid VAT-rates (R003)
- The specification lines should only use valid specifications (R069)
- The specification lines should only use valid remarks in the 'utvalgt merknad' field (R070)
- The VAT return should only use a valid remark in the 'utvalgt merknad' field (R071)

Two logistical rules are also defined for the purpose of preventing early submission to the new system or submission of earlier VAT returns:

- The submission and validation service is not available before 01.01.2023 for claim for compensation VAT returns (R090)
- The submission and validation of claim for compensation VAT returns from before 2023 is not available (R092)

## Detailed description of the validation rules

Validation of the VAT return is implemented with a set of rules that are run automatically to check the validity of the message.
The rules are designed so that they are both documentation of the rules for the message and runnable by the system.

Example of rule:

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

Each line can be translated to the following:

** Line 1 - Identifier **: This is the reference for the rule. Each rule has a unique identifier.

** Line 2 - Error message **: This is the error message that will be returned in the validation API if The VAT return is not in accordance with the requirement in the rule.

** Line 3-7 - Validation Rule **: This is the rule that defines what a valid VAT return should be.
If this rule is not met, the validation will fail.

** Line 8 - Severity **: This is the severity if the validation fails.
The following severity levels are defined : AVVIKENDE_SKATTEMELDING (anomalous VAT return), UGYLDIG_SKATTEMELDING (invalid vat return)

##Detailed Specification of the rules

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
