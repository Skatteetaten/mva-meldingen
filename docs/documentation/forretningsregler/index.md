---
icon: "cloud"
title: "Forretningsregler"
description: ""
---

## Oversikt over gjeldende forretningsregler

| Entitet                        | Attributt                                                                                                                                                                     |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SkattemeldingForMerverdiavgift | Skattepliktig.organisasjonsnummer + SkatteMeldingForMerverdiAvgift.meldingskategori + SkattegrunnagOgBeregnetSkatt.skattleggingsperiode + Innsending.regnskapssystemreferanse |
| MvaSpesifikasjonslinje         | mvaKode + spesifikasjon + mvaKodeRegnskapssystem + sats                                                                                                                       |

Regler for mva-melding:

- Start eller sluttdato for skattleggingsperioden må være innenfor registreringsdato og
  opphørsdato i Enhetsregisteret
- Skattepliktig som inngår i fellesregistrering for skattleggingsperioden uten å være
  rapporterende selskap kan ikke levere skattemelding
- Part som ikke er mva-pliktig for skattleggingsperioden og som leverer mva-melding av
  kategori alminnelig, kan bare benytte mvaKode 51, 87, 89 eller 92
- Skattepliktig må vær registrert med primærnæring for å levere skattemelding av kategori
  primærnæring
- Skattemelding av kategori kompensasjon skal dekke, og bare inneholde, informasjon som
  gjelder lov om merverdiavgiftskompensasjon
- Skattemelding av kategori primær skal dekke, og bare inneholde, informasjon som gjelder
  primærnæring. Unntak: dersom årsomsetningen for alminnelig næring er mindre enn kr 30000
  kan alminnelig næring inkluderes.
- Skattemelding av kategori alminnelig skal dekke øvrig omsetning og fradrag for
  merverdiavgift.
- Skattemelding av kategori kompensasjon kan bare benytte mvaKode 1, 11, 12, 13, 14, 15, 21,
  22, 81, 82, 83, 84, 86, 87, 88 eller 89
- Skattepliktig som er registrert i forenklet registreringsordning for skattleggingsperioden kan
  bare benytte mvaKode 3
- Grunnlag fylles ut bare når mvaKode viser utgående mva, kjøp med omvendt avgiftsplikt eller
  importmva
- Sats skal fylles ut når og bare når grunnlag er fylt ut
- Når Spesifikasjon er TapPåKrav må mvaKode være 1
- Når Spesifikasjon er Justering eller tilbakeføringAvInngåendeMerverdiavgift må mvaKode
  være 1
- Når Spesifikasjon er Uttak må mvaKode være 3, 31, 32 eller 33
- Når Spesifikasjon er tilbakeføringAvInngåendeMerverdiavgift kan bare mvaKode 1, 11, 12, 13,
  14, 15, 21, 22, 81, 82, 83, 84, 86, 87, 88 eller 89 benyttes

[regler-mvamelding.pdf](regler-mvamelding.pdf)
