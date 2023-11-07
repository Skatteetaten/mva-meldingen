---
icon: "cloud"
title: "Validation rules - VAT return for reverse tax liability"
description: "Validation rules for the VAT return for reverse tax liability"
---

[Norwegian](https://skatteetaten.github.io/mva-meldingen/omvendt/forretningsregler/)

### Change log

<table align=center>
	<tr><th style="width:25%" align=left>Date</th><th align=left> What was changed? </th></tr>
<tr>
      <td>2023.01.26</td>
      <td>
          <ul>
            <li> Added page for validation rules for VAT return for reverse tax liability</li>
          </ul>      
      </td>
    </tr>
</table>

## Validation rules

The validation rules are under development an new validation rules will be added.

The following validation rules are defined for all VAT returns:

- The sum of the calculated VAT from each VAT line shall be equal to the total VAT in the VAT return (R018)
- The calculated VAT must be in accordance with the stated VAT-basis multiplied by the current VAT-rate (R019)
- The tax return must be an ordinary (general or primary industry) VAT return, claim for compensation or VAT return for reverse tax liability (R104)
- Specification lines that apply to the reversal of input VAT given in VAT §9-6 and §9-7 require a remark (R078)
- KID numbers must be valid (R079)
- Values must not contain decimals (R082)
- Values in the basis field must be under a maximum value (R085)
- Remarks must be valid for the given VAT code (expected VAT direction) (R074)
- Remarks must be valid for the given VAT code (opposite VAT direction) (R075)
- Remarks must be valid for the given VAT code (lines with a specification) (R076)
- Specification lines that apply to purchases eligible for compensation must have basis and VAT rate (R116)
- VAT values in code lines should have a lower value than the VAT-basis value (R122)
- The VAT return cannot be submitted before the period has ended (R120)

The following validation rules are defined for VAT returns for reverse tax liability:

- The tax periode length must be 3 months (R106)
- Additional information is lacking for output VAT amounts with opposite +/- sign (R108)
- Specification lines must have valid VAT codes (R113)
- The VAT return must contain code lines when an amount has been specified in the 'fastsatt merverdiavgift' field (R107)
- Output VAT must be declared with a VAT-basis and VAT-rate (R109)
- Values for both the VAT code and a specification line should not be declared (R112)
- Specification lines relating to the reversal of input VAT, losses on outstanding claims and withdrawals can not be sent in on reverse tax liability VAT returns (R110)
- Specification lines relating to purchases eligible for compensation can only be sent in on VAT codes 86, 88 and 91 (R111)
- Declared VAT amounts on code lines do not tally with the total declared VAT amount in the 'fastsatt merverdiavgift' field (R119)
- The 'fastsatt merverdiavgift' (total declared VAT amount) should not be kr 0 (R118)
- The sum of the VAT basis values must be more than kr 2 000 (R117)
- There exists an active registration in the VAT register for at least part of the VAT period to which the reverse liability VAT return applies (R123)
- The specification line for this code must be declared with the specification 'Kjøp med kompensasjonsrett' (purchases with right to compensation) (R124)

The following technical rules are defined for the purpose of validating the format and code lists in the tax return:

- The VAT return should be in a valid format (R001)
- The specification lines should only use valid VAT codes (R002)
- The specification lines should only use valid VAT-rates (R003)
- The specification lines should only use valid specifications (R069)
- The specification lines should only use valid remarks in the 'utvalgt merknad' field (R070)
- The VAT return should only use a valid remark in the 'utvalgt merknad' field (R071)

Two logistical rules are also defined for the purpose of preventing early submission to the new system or submission of earlier VAT returns:

- The submission and validation service is not available before 01.02.2023 for reverse tax liability VAT returns (R105)
- The submission and validation of reverse tax liability VAT returns from before 2023 is not available (R103)

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
        "Det skal ikke føres beløp for koden i tillegg til spesifikasjon."
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
        "Mva-meldinger for omvendt avgiftsplikt kan kun sendes inn med terminlengde tre-månedlig."
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
    MVA_OMVENDT_AVGIFTSPLIKT_AKTIV_MVA_PLIKT_FOR_SAMME_PERIODE(
        "Merverdiavgiftsregisteret viser at dere skal levere ordinær mva-melding for denne perioden. Kjøp av tjenester fra utlandet, klimakvoter og gull skal rapporteres på ordinær mva-melding."
        {
            valideringsregel {
                meldingskategori er omvendtAvgiftsplikt såSkal { virksomhetenErIkkeRegistrertMedEnPliktForHelePerioden }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R121 }
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
    MVA_OMVENDT_AVGIFTSPLIKT_AKTIV_MVA_PLIKT_FOR_DELER_AV_PERIODEN(
        "Merverdiavgiftsregisteret viser at dere skal levere ordinær mva-melding for deler av denne perioden. Er dere sikre på at dere også skal levere mva-melding for omvendt avgiftsplikt?."
        {
            valideringsregel {
                meldingskategori er omvendtAvgiftsplikt såSkal { virksomhetenErIkkeRegistrertMedEnPliktForDelerAvPerioden }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R123 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_SPESIFIKASJON_MANGLER(
        "Koden må inneholde spesifikasjon 'kjøp med kompensasjonsrett'."
        {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) såSkal {
                    mvaSpesifikasjonslinje
                            .hvor { linje -> linje.mvaKode væreMedI mvaKodene(86, 88, 91) }
                            .skal { linje -> linje.spesifikasjon ha innhold og (linje.spesifikasjon er KOMPENSASJONSRETT.spesifikasjon.kode) }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R124 }
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
        "Innsendte koder stemmer ikke med beløpet oppgitt i 'fastsatt merverdiavgift'." {
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
        "Det må fylles ut gyldig merknad på kode med motsatt fortegn."
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
        "Dere skal ikke sende inn mva-melding for omvendt avgiftsplikt når beløpet i 'fastsatt merverdiavgift' er 0 kroner."
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
        "Grunnlaget er under 2000 kroner. Merverdiavgift skal beregnes hvis samlet kjøp for terminen overstiger denne minstegrensen." {
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
    MVA_OMVENDT_AVGIFTSPLIKT_AKTIV_MVA_PLIKT_FOR_DELER_AV_PERIODEN(
        "Det finnes en aktiv plikt i mva-registeret for deler av perioden mva-meldingen for omvendt avgiftsplikt gjelder for."
        {
            valideringsregel {
                meldingskategori er omvendtAvgiftsplikt såSkal { virksomhetenErIkkeRegistrertMedEnPliktForDelerAvPerioden }
            }
            alvorlighetsgrad { AVVIKENDE_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R123 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_SPESIFIKASJON_MANGLER(
        "Koden må inneholde spesifikasjon 'Kjøp med kompensasjonsrett."
        {
            valideringsregel {
                (meldingskategori er omvendtAvgiftsplikt) såSkal {
                    mvaSpesifikasjonslinje
                        .hvor { linje -> linje.mvaKode væreMedI mvaKodene(86, 88, 91) }
                        .skal { linje -> linje.spesifikasjon ha innhold og (linje.spesifikasjon er KOMPENSASJONSRETT.spesifikasjon.kode) }
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSKATEGORI }
            regelnummer { R124 }
        }
    ),
    MVA_OMVENDT_AVGIFTSPLIKT_MELDINGSINNHOLD_UGYLDIG_SPESIFIKASJONSLINJE(
        "Dere kan ikke bruke denne spesifikasjonen i mva-meldingen for omvendt avgiftsplikt."
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
        "Spesifikasjonen 'Kjøp av tjenester fra utlandet med kompensasjonsrett' kan kun sendes inn på kode 86 og 88. Spesifikasjonen 'Kjøp av klimakvoter og gull med kompensasjonsrett' kan kun sendes inn på kode 91."
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
    ),
    MVA_SKATTLEGGINGSPERIODEN_FOR_OPPGITT_MELDINGSKATEGORI_OMVENDT_AVGIFTSPLIKT_MÅ_VÆRE_FERDIG(
        "Meldingen kan ikke sendes inn før terminen har utløpt."
        {
            valideringsregel {
                meldingskategori er omvendtAvgiftsplikt såSkal {
                    (innsendingstidspunkt væreEtter skatteleggingsperiodeSluttdato) medmindre
                            (
                                    (innsendingstidspunkt erEtterEllerLik skatteleggingsperiodeStartdato) og
                                            (skattePliktigErSlettetFraER eller skattepliktigHarRegistrertKonkurs eller skattepliktigErKonkursbo eller ENKharDødsbo)
                                    )
                }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
            kategori { MELDINGSINNHOLD }
            regelnummer { R120 }
        }
    )

```
