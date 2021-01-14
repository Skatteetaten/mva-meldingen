---
icon: "cloud"
title: "Business rules"
description: "Business rules for the VAT tax return"
---

## Validation rules

The validation rules are under development an new validation rules will be added.
The following validation rules are definded for the VAT return listing:

- The sum of the calculated VAT from each VAT line shall be equal to the total VAT in the VAT return
- The calculated VAT must be in accordance with the stated grunnlag times the current sats
- Amounts with the opposite sign that apply to outbound tax must have a merknad
- Amounts with the opposite sign that apply to deducted inbound tax shall have a merknad
- Spesifikasjon line that applies to justering can only be submitted on VAT code 1
- Spesifikasjon line that applies to tap på krav can only be submitted on VAT code 1, 11, 12 or 13
- Spesifikasjon line that applies to uttak can only be submitted on VAT code 3, 31, 32 or 33
- Spesifikasjon line that applies to the tilbakeføring of inbound VAT given in VAT §9-6 and §9-7 can only be submitted on VAT code 1
- In the event of a omvendt avgiftsplikt for services purchased from abroad with the right to deduct shall the amount deducted in inbound tax shall be less than or equal to the outbound tax
- In the event of a omvendt avgiftsplikt for services purchased from abroad with the right to deduct, shall inbound tax can always be deducted if inbound tax is calculated
- When buying goods from abroad with a right to deduct, it must always be outbound
  fee if inbound tax has been deducted
- When buying goods from abroad with a right to deduct, it must always be deductible
  inbound tax if outgoing tax has been calculated
- In the event of a reverse charge for services purchased from abroad with the right to deduct shall
  there will always be an outgoing tax if the inbound tax has been deducted
- When purchasing goods from abroad with a right to deduct, the amount deducted in ingoing tax be less than or equal to outgoing tax

## Description of detailed validation rules

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
[8]            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
[9]        }
[10]    )
```

Each line can be translated to the following:

** Line 1 - Identifier **: This is the reference for the rule. Each rule has a unique identifier.

** Line 2 - Error message **: This is the error message that will be returned in the validation API if The VAT return is not in accordance with the requirement in the rule.

** Line 3-7 - Validation Rule **: This is the rule that defines what a valid VAT return should be.
If this rule is not met, the validation will fail.

** Line 8 - Severity **: This is the severity if the validation fails.
The following severity levels are defined : AVVIKENDE_SKATTEMELDING (deviant VAT return, MANGELFULL_SKATTEMELDING (inadequate VAT return), UGYLDIG_SKATTEMELDING (invalid vat return)

##Detailed Spesifikasjon of the rules

```kotlin

    MvaMeldingsinnhold_SumMva_FeilSummeringAvAvgiftlinjer(
        "Summen av merverdiavgift for hver avgiftslinje er ikke lik feltet fastsattMerverdiavgift" {

            valideringsregel {
                mvaSpesifikasjonslinje.summenAv { linje ->
                    linje.merverdiavgift
                } skalVære skattegrunnlagOgBeregnetSkatt.fastsattMerverdiavgift
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
        }
    ),
    MvaMeldingsinnhold_GrunnlagGangerGjeldendeSats_FeilBeregnetMerverdiavgiftForAvgiftslinje(
        "Beregnet avgift i avgiftslinje er ulik produktet av grunnlag og sats" {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.grunnlag ikkeEr tomt }
                    .skal { linje -> linje.grunnlag * linje.sats væreRundetNedTil linje.merverdiavgift }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
        }
    ),

    MvaMeldingsinnhold_Utgående_MotsattFortegn_MerknadTilMvaKodenMangler(
        "Merknad til beløp med motsatt fortegn som gjelder grunnlag og utgående avgift negativt mangler"
        {
            valideringsregel {

                utgåendeMvaSpesifikasjonslinjer
                    .hvor { linje -> linje.grunnlag erStørreEnn 0.0 }
                    .skal { linje -> linje.merknad?.beskrivelse ha innhold }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
        }
    ),

    MvaMeldingsinnhold_Inngående_MotsattFortegn_MerknadTilMvaKodenMangler(
        "Merknad til beløp med motsatt fortegn som gjelder fradragsført inngående avgift mangler"
        {
            valideringsregel {
                inngåendeMvaSpesifikasjonslinjer
                    .hvor { linje -> linje.grunnlag er tomt og (linje.merverdiavgift erMindreEnn 0.0) }
                    .skal { linje -> linje.merknad?.beskrivelse ha innhold }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_MELLOM_UTGÅENDE_OG_INNGÅENDE_AVGIFT_MVA_KODE_81(
        "Fradragsført inngående avgift som gjelder varer kjøpt fra utlandet med fradragsrett, skal være mindre enn eller lik utgående avgift"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "81" og (linje.merverdiavgift erMindreEnn 0.0) } såSkal {
                    utgåendeMerverdiavgiftMvaKode { "81" } uansetFortegnVæreStørreEnn inngåendeMerverdiavgiftMvaKode { "81" }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_MELLOM_UTGÅENDE_OG_INNGÅENDE_AVGIFT_MVA_KODE_83(
        "Fradragsført inngående avgift som gjelder varer kjøpt fra utlandet med fradragsrett, skal være mindre enn eller lik utgående avgift"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "83" og (linje.merverdiavgift erMindreEnn 0.0) } såSkal {
                    utgåendeMerverdiavgiftMvaKode { "83" } uansetFortegnVæreStørreEnn inngåendeMerverdiavgiftMvaKode { "83" }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_MELLOM_UTGÅENDE_OG_INNGÅENDE_AVGIFT_MVA_KODE_86(
        "Fradragsført inngående avgift som gjelder tjenester kjøpt fra utlandet med fradragsrett skal være mindre enn eller lik utgående avgift"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "86" og (linje.merverdiavgift erMindreEnn 0.0) } såSkal {
                    utgåendeMerverdiavgiftMvaKode { "86" } uansetFortegnVæreStørreEnn inngåendeMerverdiavgiftMvaKode { "86" }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_MELLOM_UTGÅENDE_OG_INNGÅENDE_AVGIFT_MVA_KODE_88(
        "Fradragsført inngående avgift som gjelder tjenester kjøpt fra utlandet med fradragsrett skal være mindre enn eller lik utgående avgift"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "88" og (linje.merverdiavgift erMindreEnn 0.0) } såSkal {
                    inngåendeMerverdiavgiftMvaKode { "88" } uansetFortegnVæreStørreEnn utgåendeMerverdiavgiftMvaKode { "88" }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_UTGÅENDE_AVGIFT_MANGLER_MVA_KODE_81(
        "Utgående avgift skal være beregnet dersom det er ført fradrag for inngående avgift som gjelder kjøp av varer fra utlandet med fradragsrett"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "81" og (linje.merverdiavgift erStørreEnn 0.0) } såSkal {
                    mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "81" og (linje.merverdiavgift erMindreEnn 0.0 og (linje.grunnlag ha innhold)) }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_UTGÅENDE_AVGIFT_MANGLER_MVA_KODE_83(
        "Utgående avgift skal være beregnet dersom det er ført fradrag for inngående avgift som gjelder kjøp av varer fra utlandet med fradragsrett"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "83" og (linje.merverdiavgift erStørreEnn 0.0) } såSkal {
                    mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "83" og (linje.merverdiavgift erMindreEnn 0.0 og (linje.grunnlag ha innhold)) }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_UTGÅENDE_AVGIFT_MANGLER_MVA_KODE_86(
        "Utgående avgift skal være beregnet dersom det er ført fradrag for inngående avgift som gjelder tjenester kjøpt fra utlandet med fradragsrett"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "86" og (linje.merverdiavgift erStørreEnn 0.0) } såSkal {
                    mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "86" og (linje.merverdiavgift erMindreEnn 0.0 og (linje.grunnlag ha innhold)) }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_UTGÅENDE_AVGIFT_MANGLER_MVA_KODE_88(
        "Utgående avgift skal være beregnet dersom det er ført fradrag for inngående avgift som gjelder tjenester kjøpt fra utlandet med fradragsrett"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "88" og (linje.merverdiavgift erStørreEnn 0.0) } såSkal {
                    mvaSpesifikasjonslinje.finnes { linje -> linje.mvaKode er "88" og (linje.merverdiavgift erMindreEnn 0.0 og (linje.grunnlag ha innhold)) }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_INNGÅENDE_AVGIFT_MANGLER_MVA_KODE_81(
        "Det skal være fradragsført inngående avgift dersom det er beregnet utgående avgift ved kjøp av varer fra utlandet med fradragsrett"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje ->
                    linje.mvaKode er "81" og (linje.merverdiavgift erMindreEnn 0.0)
                } såSkal {
                    mvaSpesifikasjonslinje.ikkeFinnes { linje -> linje.mvaKode er "81" og (linje.merverdiavgift er 0.0) }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_OMVENDT_AVGIFTSPLIKT_FOR_TJENSTER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_INNGÅENDE_AVGIFT_MANGLER_MVA_KODE_83(
        "Det skal være fradragsført inngående avgift dersom det er beregnet utgående avgift ved kjøp av varer fra utlandet med fradragsrett"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje ->
                    linje.mvaKode er "83" og (linje.merverdiavgift erMindreEnn 0.0)
                } såSkal {
                    mvaSpesifikasjonslinje.ikkeFinnes { linje -> linje.mvaKode er "83" og (linje.merverdiavgift er 0.0) }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_INNGÅENDE_AVGIFT_MANGLER_MVA_KODE_86(
        "Det skal være fradragsført inngående avgift dersom det er beregnet utgående avgift for tjenester kjøpt fra utlandet med fradragsrett"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje ->
                    linje.mvaKode er "86" og (linje.merverdiavgift erMindreEnn 0.0)
                } såSkal {
                    mvaSpesifikasjonslinje.ikkeFinnes { linje -> linje.mvaKode er "86" og (linje.merverdiavgift er 0.0) }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_VARER_KJØPT_FRA_UTLANDET_MED_FRADRAGSRETT_AVVIK_INNGÅENDE_AVGIFT_MANGLER_MVA_KODE_88(
        "Det skal være fradragsført inngående avgift dersom det er beregnet utgående avgift for tjenester kjøpt fra utlandet med fradragsrett"
        {
            valideringsregel {
                mvaSpesifikasjonslinje.finnes { linje ->
                    linje.mvaKode er "88" og (linje.merverdiavgift erMindreEnn 0.0)
                } såSkal {
                    mvaSpesifikasjonslinje.ikkeFinnes { linje -> linje.mvaKode er "88" og (linje.merverdiavgift er 0.0) }
                }
            }
            alvorlighetsgrad { MANGELFULL_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_SPESIFIKASJONSLINJE_TAP_PÅ_KRAV_FØRT_PÅ_FEIL_MVA_KODE(
        "Spesifikasjonslinje som gjelder tap på krav kan kun sendes inn på mva-kode 1, 11, 12 eller 13"
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.spesifikasjon er TAP_PAA_KRAV }
                    .skal { linje -> linje.mvaKode væreMedI tapPåKravLinjer }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_SPESIFIKASJONSLINJE_UTTAK_FØRT_PÅ_FEIL_MVA_KODE(
        "Spesifikasjonslinje som gjelder uttak kan kun sendes inn på mva-kode 3, 31, 32 eller 33"
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.spesifikasjon er UTTAK }
                    .skal { linje -> linje.mvaKode væreMedI uttakLinjer }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_SPESIFIKASJONSLINJE_JUSTERING_FØRT_PÅ_FEIL_MVA_KODE(
        "Spesifikasjonslinje som gjelder uttak kan kun sendes inn på mva-kode 1"
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.spesifikasjon er JUSTERING }
                    .skal { linje -> linje.mvaKode være "1" }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
        }
    ),

    MVA_MELDINGSINNHOLD_SPESIFIKASJONSLINJE_TILBAKEFØRING_INNGÅENDE_AVGIFT_9_6_OG_9_7_FØRT_PÅ_FEIL_MVA_KODE(
        "Spesifikasjonslinje som gjelder tilbakeføring av inngående mva gitt i mval §9-6 og §9-7 kan kun sendes inn på mva-kode 1"
        {
            valideringsregel {
                mvaSpesifikasjonslinje
                    .hvor { linje -> linje.spesifikasjon er TILBAKEFOERING_AV_INNGAAENDE_MERVERDIAVGIFT }
                    .skal { linje -> linje.mvaKode være "1" }
            }
            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
        }
    )

```

The validation rules are under development an new validation rules will be added.
The following validation rules are definded for the VAT return listing:

- End date for the taxation period must be earlier than the end date in the Enhetsregister (if it is given)
- Taxpayer that is included in a registration as one taxable person (VAT-law 2-2 (3)) and who files the VAT return must be reporting taxpayer for the taxation period.
- A legal entity that is not registered in the VAT register for the taxation period, and who files a VAT tax return, can only use the mvaKode 51, 87, 89 or 92
- The taxpayer must be registered as "primærnæring" in order to file a VAT tax return of the category "primær"
- VAT return of the category "kompensasjon" must contain, and only contain, information that is described in the law of VAT compensation
- VAT tax return of category "primær" must contain, and only contain, information that covers the primary industries. Exception: if the yearly turnover in other industries is less then NOK 30000 information from other industries may be included
- VAT tax return of category "alminnelig" is to cover all other turnover and deductions for VAT
- VAT tax return of category "kompensasjon" can only include mvaKode 1, 11, 12, 13, 14, 15, 21, 22, 81, 82, 83, 84, 86, 87, 88 or 89
- Taxpayers that are registered for the simplified registration scheme for the taxation period can only use mvaKode 3
- grunnlag and sats is to be filled in when mvaKode is for outbound VAT regarding turnover, "uttak", the recipient of the goods or services is liable for the VAT or import of goods or services
- grunnlag and sats is not to be filled in for inbound VAT
- When spesifikasjon equals "TapPåKrav" the mvaKode must be 1, 11, 12, 13
- When spesifikasjon equals "Justering" or “tilbakeføringAvInngåendeMerverdiavgift" the mvaKode must be 1
- When spesifikasjon equals "Uttak" the mvaKode must be in 3, 31, 32 or 33

## Business rules for the VAT tax return

Unique identification

| Entity                         | Attribute                                                                                                                                                                     |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SkattemeldingForMerverdiavgift | Skattepliktig.organisasjonsnummer + SkatteMeldingForMerverdiAvgift.meldingskategori + SkattegrunnagOgBeregnetSkatt.skattleggingsperiode + Innsending.regnskapssystemreferanse |
| MvaSpesifikasjonslinje         | mvaKode + spesifikasjon + sats                                                                                                                                                |

The rules for SAF-t codes applies to the VAT return in the same manner as for SAF-T. The documentation for the rules may be found at https://www.skatteetaten.no/globalassets/bedrift-og-organisasjon/starte-og-drive/rutiner-regnskap-og-kassasystem/saf-t-regnskap/norwegian-saf-t-standard-vat-codes.pdf,

| Norwegian term                         | English term                                          |
| -------------------------------------- | ----------------------------------------------------- |
| Grunnlag                               | Basis of calculation of VAT                           |
| mvaKode                                | VAT code                                              |
| Kompensasjon                           | Compensation, regulated by the "VAT compensation act" |
| Primær                                 | Primary industries like agriculture                   |
| alminnelig                             | Common industries                                     |
| mvaKode                                | VAT code according to SAF-T standard                  |
| sats                                   | VAT rate                                              |
| TapPåKrav                              | Lost claims                                           |
| Uttak                                  | Delivery of goods or services without renumeration    |
| tilbakeføringAvInngåendeMerverdiavgift | Reversal of deductions of VAT                         |
| Spesifikasjon                          | Spesifikasjon                                         |

Test cases may be found in the [Test page](/english/test/)
