---
icon: "cloud"
title: "Information models, XSD and encoding"
description: "XSD for VAT return for reverse tax liability (mva-melding for omvendt avgiftsplikt)
- XSD for submission of metadata information 
- encoding in XML-format"
---

[Norwegian](https://skatteetaten.github.io/mva-meldingen/omvendt/informasjonsmodell/)

# XSD for the VAT return for reverse tax liability

### Change log

| Date       | What changed?                                                                     |
| :--------- | :-------------------------------------------------------------------------------- |
| 2023.01.30 | Initial version of documentation for VAT return for reverse tax liability         |


## Change in the code list for as a consequence of the VAT return for reverse tax liability

In the code list for remarks (merknad.xml) and SAFT-T (mvaKodeSAFT.xml) the following has been added:

    <omvendtAvgiftsplikt>SANN</omvendtAvgiftsplikt>


These additions shal be used to decide if the code pertains to reverse liability.

Notice that when the ERP suppliers start using the new version of the code list they will have to adapt to these code list additions.
Codes will then be chosen based on whether or not the code has the code addition (kodetillegg) omvendtAvgiftsplikt=SANN, kompensasjon=SANN or alminneligPrimær=SANN.

## Version 1.0 of the XSD for VAT return for reverse tax liability

VAT return for reverse tax liability must be submitted in XML-format. It must be in accordance with the structure outlined for the VAT-return. The same XSD applies for all returns.
Version 1.0 of this XSD is found here [no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd)

Graphical representation of the XSD and encoding for the [VAT return for reverse tax liability](SkattemeldingForMerverdiavgiftKompensasjon.jpg):

![SkattemeldingForMerverdiavgift2020](SkattemeldingForMerverdiavgiftOmvendt.jpg)

Example files for VAT return for reverse tax liability in XML format can be downloaded [here](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/informasjonsmodell_filer/example_files/melding)

## Description of the fields in the VAT return for reverse tax liability

### Mva-melding for omvendt avgiftsplikt (VAT return for reverse tax liability)

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>meldingskategori</td><td>The subtype of the return <br>
	Purpose: to ensure that the user can fulfill their VAT reporting obligations
	</td>
  </tr>
    <tr><td>merknad</td><td>Additional information about the content of the  VAT return for reverse tax liability<br>
	Purpose: to ensure that the taxpayer have the possibility to explain their application of law when necessary
	</td>
  </tr>
</table>

### Skattepliktig (Taxable organization)

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>organisasjonsnummer</td><td>Unique identifier for the taxable organisation  <br>
  Purpose: to take care of the rights and obligations of the taxpayer
	</td>
  </tr>	
</table>

### Innsending (Submission)

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

### Betalingsinformasjon (Payment information)

KID is only applicable if the business is to get VAT back from the Tax Authority.

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>KID</td><td>The recipient's identification of a payment <br>
Purpose: To be able to pay to the bank accounts that require KID 
</table>

### Skattegrunnlag og beregnet skatt (Tax basis and calculated tax)

<table align=center>
  <tr><th style="width:25%" align=left>Field</th><th align=left>Description</th></tr>
  <tr><td>skattleggingsperiode</td><td>The taxation period for which the  VAT return for reverse tax liability applies <br>
  Period is stated in accordance with the code list for the Skattleggingsperiode. 
For the VAT return for reverse tax liability quarterly period applies. <br>
Purpose: to ensure consistency between bookkeeping and VAT return period 
	</td>
  </tr>
    <tr><td>fastsattMerverdiavgift</td><td>Sum to pay / sum to be refunded <br>
Purpose: to ensure that the correct amount is being paid
	</td>
  </tr>
</table>

### MvaSpesifikasjonslinje (VAT-specification line)

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
  <tr><td>mvaKodeRegnskapssystem</td><td>Internal VAT code in the accounting system. There may be several internal VAT codes for a mvaKode and possibly a specification. In that case, there will be several lines in the VAT return for reverse tax liability per mvaKode and specification; one per combination of VAT code, specification and VAT CodeAccounting system. <br>
Purpose: Two considerations <br>
Users: recognizable in relation to what they see in the accounting system. <br>
The system suppliers will not have to change VAT codes in the systems
	</td>
  </tr>
  <tr><td>grunnlag</td><td>The amount of which VAT is calculated. <br>
Purpose: Basis for control from the Tax Administration
	</td>
  </tr>
  <tr><td>sats</td><td>The VAT rate used in calculating VAT.<br>
Purpose: To ensure that only valid rates are used for calculating VAT 
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

## Description of the fields in the VAT return for reverse tax liability submission

### MvaMeldingInnsending (VAT return submission)

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
        A VAT return with meldingskategori alminnelig, primær and omvendtAvgiftsplikt will always be <strong>komplett</strong>. <br>
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
	
### Identifikator (Identifier, Either organisasjonsnummer or foedselsnummer)
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
	
### Skattleggingsperiode (taxation period)
<table align=center>
  <tr><th style="width:25%" align=left>Felt</th><th align=left>Description</th></tr>
  <tr>
    <td>periode</td>
    <td>
        The taxation period for which the  VAT return for reverse tax liability applies <br>
  Period is stated in accordance with the code list for the Skattleggingsperiode. 
For the  VAT return for reverse tax liability quarterly period applies. <br>
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
	
### Vedlegg (Attachment)
<table align=center>
  <tr><th style="width:25%" align=left>Felt</th><th align=left>Description</th></tr>
  <tr>
    <td>vedleggstype</td>
    <td>
        Type of attachments which is uploaded to the instance on Altinn.
        Where you can either use <strong>mva-melding</strong> for the tax return for VAT return for reverse tax liability , or <strong>binaerVedlegg</strong> for general attachments.
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
	
### Vedleggsfil (Attachment file)
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

## Encoding (code List)

| Group and code                                                      | Description of code and specification                                               |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Purchases without deductions					      |                                                                                     |
| 87                                                                  | Purchases of goods from abroad without deduction (standard rate)	            |
| 89								      | Purchases of goods from abroad without deduction (low rate)                         |
| 92                                                                  | Purchases of emission allowances and gold without deduction		            |
| Purchases without deductions					      |											    |
| 86								      | Purchases of services from abroad with compensation for VAT (standard rate)	    |
| 88                                                                  | Purchases of services from abroad with compensation for VAT (low rate)              |
| 91								      | Purchases of emission allowances and gold with compensation for VAT (standard rate) |


[Overview of encoding/ code list:](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/informasjonsmodell_filer/kodelister/)

- Encoding for VAT code: [mvaKodeSAFT](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/kodelister/mvaKodeSAFT.xml)
- Encoding for VAT specification: [mvaSpesifikasjon](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/kodelister/mvaSpesifikasjon.xml)
- Encoding for VAT rate: [sats](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/kodelister/sats.xml)
- Encoding for remarks: [merknader](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/kodelister/merknad.xml)
- Encoding for remarks and corresponding VAT code: [merknadTilsvarendeMvaKode.xml](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/kodelister/merknadTilsvarendeMvaKode.xml)

# XSD for uploading metadata

The submission of the VAT return requires an XML file containg metadata. This file must be according to the XSD for submission.

[no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/xsd/no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd)

# XSD for validation response

XSD for validation documents the structure of the response from the validation service. The feedback will also be according to this XSD.
[no.skatteetaten.fastsetting.avgift.mva.valideringsresultat.v1.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/xsd/no.skatteetaten.fastsetting.avgift.mva.valideringsresultat.v1.xsd)

# XSD for payment information

[no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.betalingsinformasjon.v1.0.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.betalingsinformasjon.v1.0.xsd)
