---
icon: "cloud"
title: "Valideringsregler - kompensasjonsmelding"
description: "Regler for utfylling av kompensasjonsmeldingmelding "
---

### Endringslogg

<table align=center>
  <tr><th style="width:25%" align=left>Dato</th><th align=left> Hva ble endret? </th></tr>
    <tr>
      <td>2022.05.18</td>
      <td>
          <ul>
            <li> R085 sjekk at beløpet på grunnlaget er mindre enn maks verdi"</li>
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
- Merknad til beløp med motsatt fortegn som gjelder fradragsført inngående avgift mangler
- Merknad til beløp med motsatt fortegn som gjelder spesifikasjonslinje for tilbakeføring av inngående mva. gitt i mval §9-6 og §9-7
- Mva-meldingen skal ikke sendes inn før gjeldende skattleggingsperiode er ferdig (alminnelig)
- Inngående mva. skal føres uten grunnlag og sats
- Kontonummer må være registrert for meldinger som kunne føre til en utbetaling
- Merknader må være gyldig for brukt mva-kode (vanlig fortegn)
- Merknader må være gyldig for brukt mva-kode (motsatt fortegn)

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
