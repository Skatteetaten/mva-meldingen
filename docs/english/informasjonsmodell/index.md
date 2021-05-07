---
icon: "cloud"
title: "Information models, XSD and encoding"
description: "xsd for VAT return (mva-melding)
- XSD for filing information 
- encoding in XML-format"
---

# XSD for the VAT return

Version 1.0 of this XSD is found here [no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9](https://github.com/Skatteetaten/mva-meldingen/tree/oppdatere-regler-og-api-beskrivelse/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9.xsd)

Graphical representation of the XSD and encoding for the VAT return:

![SkattemeldingForMerverdiavgift2020](SkattemeldingForMerverdiavgift2020.png)

Simple prototype of the VAT return:

[revidert-protoype-mvamelding](revidert-protoype-mvamelding.xlsx)

Example files for VAT return in XML format can be downloaded from the test section: https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/eksempler/melding/

## Encoding

Overview of encoding/ code list: [Oversikten over kodelister](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/kodelister/)

- Encoding for VAT code: [mvaKodeSAFT](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/mvaKodeSAFT.xml)
- Encoding for VAT specification: [mvaSpesifikasjon](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/mvaSpesifikasjon.xml)
- Encoding for VAT rate: [sats](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/sats.xml)
- Encoding for remarks: [merknader](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/merknader.xml)
- Encoding for remarks and corresponding VAT code: [merknadTilsvarendeMvaKode.xml](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/merknaderTilsvarendeMvaKode.xml)

## Remarks in accordance to the VAT codes and the VAT tax return

Overview over remarks in accordance to the VAT codes in the VAT tax return [remarks in accordance to the VAT codes](merknader mot poster og hele meldingen.xlsx)

# XSD for filing metadata

The filing of the VAT return requires an XML file containg metadata. This file must be according to the XSD for filing.

[no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd)

# XSD for validation response

XSD for validation documents the structure of the response from the validation service. The feedback will also be according to this XSD.

# XSD for payment information

[no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.betalingsinformasjon.v1.0.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.betalingsinformasjon.v1.0.xsd)
