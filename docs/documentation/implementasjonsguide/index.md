---
icon: "cloud"
title: "Implementasjonsguide"
description: "En utviklers guide til implementasjonen"
---

## Implementasjonsguide

## Forord

Denne guiden er skrevet av en utvikler for å gi leverandører en oversikt over et tenkt prosjekt for å implementere elektronisk innsending av modernisert Mva-Melding til Skattetatens API'er. Guiden vil hjelpe prosjektledere og utviklere med forståelsen av omfanget og hvilke tekniske betraktninger man bør ta stilling til.

## Oversikt

|  #  | Oppgave                                                                                 | Avhengigheter | Kompleksitet |
| :-: | --------------------------------------------------------------------------------------- | :-----------: | :----------: |
|  1  | Uttrekk av grunnlagsdata fra regnskapssystemet til utfylling av modernisert Mva-Melding |       -       |   \* [^1]    |
|  2  | Visning av Mva-Meldingen i regnskapssytemet                                             |       1       |   \* [^1]    |
|  3  | ID-Porten integrasjon                                                                   |       -       |      21      |
|  4  | Validere Mva-Melding mot Skatteetatens validerings-api                                  |       3       |      1       |
|  5  | Tolkning og visning av valideringsresultatet i regnskapssystemet                        |       4       |   \* [^1]    |
|  6  | Sende Mva-Melding til Skatteetatens innsendings-api                                     |       3       |      1       |
|  7  | Hente status på innsendingen hos Skatteetatens innsendings-api                          |       3       |      2       |
|  8  | Laste ned og tolke Skatteetatens tilbakemeldinger                                       |       3       |      2       |

[^1]: Kompleksiteten i denne oppgaven er avhengig av implementasjonen av regnskapssystemet og er opp til leverandøren å evaluere.
