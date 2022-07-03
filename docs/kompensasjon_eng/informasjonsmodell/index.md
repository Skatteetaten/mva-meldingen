---
icon: "cloud"
title: "Information models, XSD and encoding"
description: "XSD for tax return for VAT compensation (kompensasjonsmelding for merverdiavgift)
- XSD for submission of metadata information 
- encoding in XML-format"
---

[Norwegian](https://skatteetaten.github.io/mva-meldingen/kompensasjon/informasjonsmodell/)

# XSD for the tax return for VAT compensation

### Change log

| Date       | What changed?                                                    |
| :--------- | :--------------------------------------------------------------- |
| 2022.06.30 | Initial version of documentation for compensation report for VAT |
|            |

## Version 1.0 of the XSD for the tax return for VAT compensation

The tax return for VAT compensation must be submitted in XML-format. It must be in accordance with the structure outlined for the VAT-return. The same XSD applies for both returns.
Version 1.0 of this XSD is found here [no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd)

Graphical representation of the XSD and encoding for the [tax return for VAT compensation](SkattemeldingForMerverdiavgiftKompensasjon.jpg):

![SkattemeldingForMerverdiavgift2020](SkattemeldingForMerverdiavgiftKompensasjon.jpg)


Example files for tax return for VAT compensation in XML format can be downloaded from the [test section](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/kompensasjon/test/eksempler/melding/)

## Description of the fields in the tax return for VAT compensation

### Tax return for VAT compensation

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>meldingskategori</td><td>The subtype of the return <br>
	Purpose: to ensure that the user can fulfill their VAT reporting obligations
	</td>
  </tr>
    <tr><td>merknad</td><td>Additional information about the content of the tax return for VAT compensation<br>
	Purpose: to ensure that the taxpayer have the possibility to explain their application of law when necessary
	</td>
  </tr>
</table>

### Skattepliktig

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>organisasjonsnummer</td><td>Unique identifier for the taxable organisation  <br>
  Purpose: to take care of the rights and obligations of the taxpayer
	</td>
  </tr>	
</table>

### Innsending

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>regnskapssystemrefereanse</td><td>The taxpayers unique reference for the submission <br>
  Purpose: To ensure that the taxpayer and the tax office refer to the same return. 
	</td>
  </tr>
    <tr><td>system</td><td>Name and possible version of accounting system <br>
Purpose: To be able to follow up systematic errors with the system supplier instead of following up each individual taxpayer. 
	</td>
  </tr>
</table>

### Payment information

KID is only applicable if the business is to get VAT back from the Tax Authority.

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>KID</td><td>The recipient's identification of a payment <br>
Purpose: To be able to pay to the bank accounts that require KID 
</table>

### Tax basis and calculated tax

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>skattleggingsperiode</td><td>The taxation period for which the tax return for VAT compensation applies <br>
  Period is stated in accordance with the code list for the Skattleggingsperiode. 
For the tax return for VAT compensation bi-monthly period applies. Businesses mentioned in the 
VAT compensation legislation (merverdiavgiftskompensasjonsloven) §2, first subparagraph letters b to e and housing associations and condominiums as mentioned in the second subparagraph may make claims that include an entire calendar year in the tax return for VAT compensation in the sixth term. <br>
Purpose: to ensure consistency between bookkeeping and VAT return period 
	</td>
  </tr>
    <tr><td>fastsattMerverdiavgift</td><td>Sum to pay / sum to be refunded <br>
Purpose: to ensure that the correct amount is being paid
	</td>
  </tr>
</table>

### MvaSpesifikasjonslinje

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>mvaKode</td><td>Classification of incoming and outgoing VAT in accordance with the Norwegian SAF-T standard <br>
Purpose: dissemination of which VAT assessments have been carried out
	</td>
  </tr>
  <tr><td>spesifikasjon</td><td>Detailing some VAT conditions that are not included in the Norwegian SAF-T standard <br>
Purpose: dissemination of which VAT assessments have been carried out
	</td>
  </tr> 
  <tr><td>mvaKodeRegnskapssystem</td><td>Internal VAT code in the accounting system. There may be several internal VAT codes for a mvaKode and possibly a specification. In that case, there will be several lines in the tax return for VAT compensation per mvaKode and specification; one per combination of VAT code, specification and VAT CodeAccounting system. <br>
Purpose: Two considerations <br>
Users: recognizable in relation to what they see in the accounting system. <br>
The system suppliers will not have to change VAT codes in the systems
	</td>
  </tr>
  <tr><td>grunnlag</td><td>The amount of which VAT is calculated. <br>
Purpose: Basis for control from the Tax Administration
	</td>
  </tr>
  <tr><td>sats</td><td>The VAT rate used in calculating VAT compensation. <br>
Purpose: To ensure that only valid rates are used for VAT compensation
	</td>
  </tr>
  <tr><td>merverdiavgift</td><td>Fixed VAT <br>
Purpose: to show calculated VAT per line
      </td>
  </tr>  
  <tr><td>merknad</td><td>Information about the content of mvaKode <br>
Purpose: to ensure that the taxpayer can explain his own application of the law where necessary 
  </tr>

</table>

## Description of the fields in the tax return for VAT compensation submission

### MvaMeldingInnsending

<table align=center>
  <tr><th style="width:25%" align=left>Felt</th><th align=left>Description</th></tr>
  <tr><td>meldingskategori</td>
    <td>
        The subtype of the form which is submitted <br>
        Purpose: to ensure that the user can fulfill their VAT reporting obligations
	</td>
  </tr>
  <tr><td>innsendingstype</td>
    <td>
        A VAT return with meldingskategori alminnelig og primær will always be <strong>komplett</strong>. An initial tax return for VAT compensation will be complete when signed by the auditor. A corrected tax return for VAT compensation will be completed upon submission. <br>
        Purpose: The field is kept so at a later date it can be opened for auditors to comment/write notes on returns (e.g. VAT compensation) that should be approved by an auditor before submission.
</td>
  </tr>
  <tr><td>instansstatus</td>
    <td>
        This field will be removed since we get the required information from the events on the instance. <br>
        This will be done by making the field optional in a transition and removed at a appropriate time.
	</td>
  </tr>
  <tr><td>opprettetAv</td>
    <td>
        This field should contain the name of the logged in user. <br>
        Purpose: The content of this field will be displayed in Altinn.
	</td>
  </tr>
  <tr><td>opprettingstidspunkt</td>
    <td>
        This field will be removed since we get the required information from the events on the instance. <br>
        This will be done by making the field optional in a transition and removed at a appropriate time.
	</td>
  </tr>
</table>

<br>
Identifier (Either organisasjonsnummer or foedselsnummer)
<table align=center>
  <tr><th style="width:25%" align=left>Felt</th><th align=left>Description</th></tr>
  <tr>
    <td>organisasjonsnummer</td>
    <td>
        Unique identifier for the taxable organisation <br>
        Purpose: to take care of the rights and obligations of the taxpayer
	</td>
  </tr>
  <tr><td>foedselsnummer</td>
    <td>
        Unique identifier for the taxable organisation <br>
        Purpose: to take care of the rights and obligations of the taxpayer
	</td>
  </tr>
</table>

<br>
Skattleggingsperiode
<table align=center>
  <tr><th style="width:25%" align=left>Felt</th><th align=left>Description</th></tr>
  <tr>
    <td>periode</td>
    <td>
        The taxation period for which the tax return for VAT compensation applies <br>
  Period is stated in accordance with the code list for the Skattleggingsperiode. 
For the tax return for VAT compensation bi-monthly period applies. Businesses mentioned in the 
VAT compensation legislation (merverdiavgiftskompensasjonsloven) §2, first subparagraph letters b to e and housing associations and condominiums as mentioned in the second subparagraph may make claims that include an entire calendar year in the tax return for VAT compensation in the sixth term. <br>
        Purpose: to ensure consistency between book keeping and VAT return period.
	</td>
  </tr>
  <tr><td>aar</td>
    <td>
        The taxation year for which the  return applies <br>
        Purpose: to ensure consistency between book keeping and VAT return period.
	</td>
  </tr>
</table>

<br>
Attachments
<table align=center>
  <tr><th style="width:25%" align=left>Felt</th><th align=left>Description</th></tr>
  <tr>
    <td>vedleggstype</td>
    <td>
        Type of attachments which is uploaded to the instance on Altinn.
        Where you can either use <strong>mva-melding</strong> for the tax return for VAT compensation , or <strong>binaerVedlegg</strong> for general attachments.
	</td>
  </tr>
  <tr><td>kildegruppe</td>
    <td>
        Which group the submission comes from. <br>
        Options: <strong>etat</strong>, <strong>sluttbrukersystem</strong>, <strong>sluttbruker</strong> 
	</td>
  </tr>
  <tr><td>opprettetAv</td>
    <td>
        This field should contain the name of the logged in user. <br>
        Purpose: The content of this field will be displayed in Altinn.
	</td>
  </tr>
  <tr><td>opprettingstidspunkt</td>
    <td>
        This field will be removed since we get the required information from the events on the instance. <br>
        This will be done by making the field optional in a transition and removed at a appropriate time.
	</td>
  </tr>
</table>

<br>
Attachment file
<table align=center>
  <tr><th style="width:25%" align=left>Felt</th><th align=left>Description</th></tr>
  <tr>
    <td>filnavn</td>
    <td>
        Name of the file which is uploaded as attachment <br>
	</td>
  </tr>
  <tr><td>filekstensjon</td>
    <td>
        The file extension for the file which is uploaded as attachment <br>
	</td>
  </tr>
  <tr><td>filinnhold</td>
    <td>
        Description of the contents of the file which is uploaded as attachment <br>
	</td>
  </tr>
</table>

## Encoding

| Group and code                                                     | Description of code, deductions and specification                                 |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Compensation for VAT on purchases of goods and services in Norway  |                                                                                   |
| 1                                                                  | Compensation for VAT (standard rate)                                              |
| Specification line for code 1                                      | Adjustment of VAT compensation for real property                                  |
| 11                                                                 | Compensation for VAT (middle rate)                                                |
| 13                                                                 | Compensation for VAT (low rate)                                                   |
| Compensation for VAT on purchases of goods from abroad (import)    |                                                                                   |
| 14                                                                 | Compensation for value added tax paid upon import (standard rate)                 |
| Specification line for code 14                                     | Adjustment of VAT compensation for real property                                  |
| 15                                                                 | Compensation for value added tax paid upon import (middle rate)                   |
| 81                                                                 | Compensation for purchases of goods from abroad (standard rate)                   |
| Specification line for code 81                                     | Adjustment of VAT compensation for real property                                  |
| 83                                                                 | Compensation for purchases of goods from abroad (middle rate)                     |
| Compensation for VAT on purchases of services from abroad (import) |                                                                                   |
| 86                                                                 | Compensation for VAT on purchases of services from abroad (standard rate)         |
| 88                                                                 | Compensation for VAT on purchases of services from abroad (low rate)              |
| Emission allowances and gold                                       |                                                                                   |
| 91                                                                 | Compensation for VAT on purchases of emission allowances and gold (standard rate) |

[Overview of encoding/ code list:](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/informasjonsmodell/kodelister/)

- Encoding for VAT code: [mvaKodeSAFT](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/mvaKodeSAFT.xml)
- Encoding for VAT specification: [mvaSpesifikasjon](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/mvaSpesifikasjon.xml)
- Encoding for VAT rate: [sats](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/sats.xml)
- Encoding for remarks: [merknader](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/merknad.xml)
- Encoding for remarks and corresponding VAT code: [merknadTilsvarendeMvaKode.xml](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/kodelister/merknadTilsvarendeMvaKode.xml)

# XSD for uploading metadata

The submission of the VAT return requires an XML file containg metadata. This file must be according to the XSD for submission.

[no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd)

# XSD for validation response

XSD for validation documents the structure of the response from the validation service. The feedback will also be according to this XSD.
[no.skatteetaten.fastsetting.avgift.mva.valideringsresultat.v1.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.valideringsresultat.v1.xsd)

# XSD for payment information

[no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.betalingsinformasjon.v1.0.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.betalingsinformasjon.v1.0.xsd)
