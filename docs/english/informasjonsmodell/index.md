---
icon: "cloud"
title: "Information models, XSD and encoding"
description: "XSD for VAT return (mva-melding)
- XSD for submission of metadata information 
- encoding in XML-format"
---

# XSD for the VAT return

### Change log

| Date       | What changed?                                                                                                                                                                                                  |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2021.06.21 | Updated code list [mvaSpesifikasjon](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/mvaSpesifikasjon.xml), correcting "tap på krav" to "tapPåKrav" |

## Version 1.0 of the XSD for the VAT return

Version 1.0 of this XSD is found here [no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0](https://github.com/Skatteetaten/mva-meldingen/tree/oppdatere-regler-og-api-Description/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd)

Graphical representation of the XSD and encoding for the [VAT return](SkattemeldingForMerverdiavgift2020.png):

![SkattemeldingForMerverdiavgift2020](SkattemeldingForMerverdiavgift2020.png)

Simple prototype of the VAT return:

[revidert-protoype-mvamelding](revidert-protoype-mvamelding.xlsx)

Example files for VAT return in XML format can be downloaded from the test section: https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/eksempler/melding/

## Description of the fields in the VAT return

### MvaMelding

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>meldingskatergori</td><td>Description: the subtype of the VAT return <br>
	Purpose: to ensure that the user can fulfill their VAT reporting obligations
	</td>
  </tr>
    <tr><td>merknad</td><td>Description: additional information about the content of the VAT return<br>
	Purpose: to ensure that the taxpayer have the possibility to explain their application of law when necessary
	</td>
  </tr>
</table>

### Skattepliktig

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>organisasjonsnummer</td><td>Description: unique identifier for the taxable organisation  <br>
  Purpose: to take care of the rights and obligations of the taxpayer
	</td>
  </tr>	
</table>

### Innsending

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>regnskapssystemrefereanse</td><td>Description: The taxpayers unique reference for the submission <br>
  Purpose: To ensure that the taxpayer and the tax office refer to the same message. 
	</td>
  </tr>
    <tr><td>system</td><td>Description: Name and possible version of accounting system <br>
Purpose: To be able to follow up systematic errors with the system supplier instead of following up each individual taxpayer. 
	</td>
  </tr>
</table>

### Betalingsinformasjon

Oppgis bare dersom det er tilgodebeløp.

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>KID</td><td>Description: The recipient's identification of a payment <br>
Purpose: To be able to pay to the bank accounts that require KID 
</table>

### Skattegrunnlag og beregnet skatt

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>skattleggingsperiode</td><td>Description: the taxation period for which the VAT return applies <br>
Purpose: to ensure consistency between bookkeeping and VAT return period 
	</td>
  </tr>
    <tr><td>fastsattMerverdiavgift</td><td>Description: sum to pay / sum to be refunded <br>
Purpose: to ensure that the correct amount is being paid
	</td>
  </tr>
</table>

### MvaSpesifikasjonslinje

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>mvaKode</td><td>Description: Classification of incoming and outgoing VAT in accordance with the Norwegian SAF-T standard <br>
Purpose: dissemination of which VAT assessments have been carried out
	</td>
  </tr>
  <tr><td>spesifikasjon</td><td>Description: detailing some VAT conditions that are not included in the Norwegian SAF-T standard <br>
Purpose: dissemination of which VAT assessments have been carried out
	</td>
  </tr> 
  <tr><td>mvaKodeRegnskapssystem</td><td>Description: internal VAT code in the accounting system. There may be several internal VAT codes for a VAT code and possibly a specification. In that case, there will be several lines in the VAT message per VATCode and specification; one per combination of VAT code, specification and VAT CodeAccounting system. <br>
Purpose: Two considerations <br>
Users: recognizable in relation to what they see in the accounting system. <br>
The system suppliers will not have to change VAT codes in the systems
	</td>
  </tr>
  <tr><td>grunnlag</td><td>Description: the amount of which VAT is calculated.
The field must not be filled in for input VAT. <br>
Purpose: Basis for control from the Tax Administration
	</td>
  </tr>
  <tr><td>sats</td><td>Description: The VAT rate used in calculating outgoing VAT. 
The field must not be filled in for incoming VAT. <br>
Purpose: To ensure that only valid rates are used for invoicing
	</td>
  </tr>
  <tr><td>merverdiavgift</td><td>Description: fixed VAT <br>
Purpose: to show calculated VAT per line
      </td>
  </tr>  
  <tr><td>merknad</td><td>Description: information about the content of mvaKode <br>
Purpose: to ensure that the taxpayer can explain his own application of the law where necessary 
  </tr>

</table>

## Encoding

[Overview of encoding/ code list:](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/kodelister/)

- Encoding for VAT code: [mvaKodeSAFT](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/mvaKodeSAFT.xml)
- Encoding for VAT specification: [mvaSpesifikasjon](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/mvaSpesifikasjon.xml)
- Encoding for VAT rate: [sats](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/sats.xml)
- Encoding for remarks: [merknader](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/merknad.xml)
- Encoding for remarks and corresponding VAT code: [merknadTilsvarendeMvaKode.xml](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/merknadTilsvarendeMvaKode.xml)

## Remarks in accordance to the VAT codes and the VAT tax return

Overview over remarks in accordance to the VAT codes in the VAT tax return [remarks in accordance to the VAT codes](merknader mot poster og hele meldingen.xlsx)

# XSD for uploading metadata

The submission of the VAT return requires an XML file containg metadata. This file must be according to the XSD for submission.

[no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd)

# XSD for validation response

XSD for validation documents the structure of the response from the validation service. The feedback will also be according to this XSD.
[no.skatteetaten.fastsetting.avgift.mva.valideringsresultat.v1.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.valideringsresultat.v1.xsd)

# XSD for payment information

[no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.betalingsinformasjon.v1.0.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.betalingsinformasjon.v1.0.xsd)
