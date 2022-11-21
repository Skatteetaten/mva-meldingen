---
icon: "cloud"
title: "Test & Produksjon"
description: "Informasjon om testing og produksjon"
---

## Endringslogg

| Dato       | Hva ble endret?                                     |
| :--------- |:----------------------------------------------------|
| 2022.15.11 | Opprettet egen side for hvordan kjøre python script |

# Test av applikasjon ved hjelp av Python script

Det er skrevet et Python script som kan brukes i forbindelse med test av løsningen mot Skatteetaten.
[Python script for henting, validering og innsending](https://github.com/Skatteetaten/mva-meldingen/blob/master/test_with_phyton_script_files/mva_melding_innnsending.py).
Klon hele repositoriet eller last ned katalogen under:

    /test_with_python_script_files

Før du kjører scriptet må du installere Python og noen biblioteker.

## Sjekk om python og pip er installert (Minimum python3 versjon 3.6.X)
    python3 --version

    pip3 --version

Hvis de ikke er installert kan de installeres gjennom terminal vindu

### Mac
    brew install python

    python3 -m pip install --upgrade pip

Eventuelt kan man bruke en versjonshåndtering pakke i stedet.
For mer informasjon rundt python på Mac kan man lese på homebrew: <br>
<a href="https://formulae.brew.sh/formula/pyenv" target="_blank">https://formulae.brew.sh/formula/pyenv <br>
<a href="https://docs.brew.sh/Homebrew-and-Python" target="_blank">https://docs.brew.sh/Homebrew-and-Python

### Linux Ubuntu
    sudo apt-get update
    sudo apt-get install python3.8
    sudo apt install python3-pip

## Installer python biblioteker
Åpne terminalen i prosjekt mappa, og naviger til 
    `/test_with_python_script` mappen. <br>
Deretter installer alt av nødvendige biblioteker. <br>
Kan eventuelt bruke en venv i stedet for å installere globalt, 
les mer her: https://docs.python.org/3/library/venv.html

    cd docs/test_with_python_script

    pip3 install -r requirements.txt

## Kjøre Python scriptet
1. Last ned katalogen `test_with_python_script` under https://github.com/Skatteetaten/mva-meldingen/tree/master/docs
2. Du må søke opp en testbruker med en tilhørende virksomhet som beskrevet i [Bruksveiledning for Tenor Testdatasøk](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/mvameldingen/test/Bruksveiledning_Tenor.pdf) .
3. Noter deg fødselsnummer til testbruker og organisasjonsnummer til den virksomheten denne testbrukeren kan sende inn for
4. Gjør endringer i følgende filer:
   1. organisasjonsnummer i filen `mva_melding_innnsending.py` (Se under kommentaren "# Legg inn org_nummer du ønsker å sende inn for"), er nå hardkodet til 999999999
   2. organisasjonsnummer i konvolutt filen du ønsker å sende inn (example_files/konvolutt)
   3. organisasjonsnummer i mva-melding filen du ønsker å sende inn (example_files/melding)
   4. eventuelt andre testdata som feks skattleggingsperiode, meldingskategori etc
   5. Oppdater filnavnene i filen `mva_melding_innnsending.py` til de filene du ønsker å benytte: 
      1. `mvaMeldingInnsending_filnavn` = "kompensasjon_mvakonvolutt.xml"
      2. `mvaMelding_filnavn` = "kompensasjon_mvamelding.xml"
   6. NB! Husk å sørg for at konvolutt og mva-melding stemmer overens i forhold til testdataene
5. Kjør Python scriptet
6. Etter at scriptet er startet så åpnes en nettleser. Trykk på "TestID" og benytt det fødselsnummer du noterte deg i steg 3)
