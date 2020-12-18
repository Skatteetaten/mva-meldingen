---
icon: "cloud"
title: "Introduksjon til Valideringsregler"
description: "Regler for utfylling av mva-melding "
---

## Valideringsregler pr. 15 desember 2020:

Valideringsreglene er under utvikling og nye valideringsregler vil bli lagt
til fortløpende.
Følgende valideringsregler er foreløpig definert for mva-meldingen pr 15. desember 2020:

- Summen av beregnet avgift fra hver avgiftslinje skal være lik sum avgift i Mva-meldingen
- Beregnet avgift skal stemme med oppgitt grunnlag ganger gjeldende sats
- Beløp med motsatt fortegn som gjelder utgående avgift skal ha en merknad
- Beløp med motsatt fortegn som gjelder fradragsført inngående avgift skal ha en merknad
- Spesifikasjonslinje som gjelder justering kan kun sendes inn på mva-kode 1
- Spesifikasjonslinje som gjelder tap på krav kan kun sendes inn på mva-kode 1, 11, 12 eller 13
- Spesifikasjonslinje som gjelder uttak kan kun sendes inn på mva-kode 3, 31, 32 eller 33
- Spesifikasjonslinje som gjelder tilbakeføring av inngående mva gitt i mva §9-6 og §9-7
  kan kun sendes inn på mva-kode 1
- Ved omvendt avgiftsplikt for tjenester kjøpt fra utlandet med fradragsrett skal
  fradragsført beløp i inngående avgift skal være mindre enn eller lik utgående avgift
- Ved omvendt avgiftsplikt for tjenester kjøpt fra utlandet med fradragsrett skal
  det alltid være fradradragsført inngående avgift dersom det er beregnet inngående avgift
- Ved kjøp av varer fra utlandet med fradragsrett skal det alltid være utgående
  avgift dersom det er fradragsført inngående avgift
- Ved kjøp av varer fra utlandet med fradragsrett skal det alltid være fradragsført
  inngående avgift dersom det er beregnet utgående avgift
- Ved omvendt avgiftsplikt for tjenester kjøpt fra utlandet med fradragsrett skal
  det alltid være utgående avgift dersom det er fradragsført inngående avgift
- Ved kjøp av varer fra utlandet med fradragsrett skal fradragsført beløp i
  inngående avgift være mindre enn eller lik utgående avgift

## Beskrivelse av detaljerte valideringsregler nedenfor

Validering av MVA-meldingen er implementert med et sett av regler som kjøres maskinelt
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
[8]            alvorlighetsgrad { UGYLDIG_SKATTEMELDING }
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
Følgende alvorlighetsgrader er definert : AVVIKENDE_SKATTEMELDING, MANGELFULL_SKATTEMELDING, UGYLDIG_SKATTEMELDING

# Detljspesifikasjon av reglene pr 15 desember 2020:

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
