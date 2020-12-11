---
icon: "cloud"
title: "Business rules"
description: "Business rules for the VAT tax return"
---

## Business rules for the VAT tax return

Unique identification

| Entity                         | Attribute                                                                                                                                                                     |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SkattemeldingForMerverdiavgift | Skattepliktig.organisasjonsnummer + SkatteMeldingForMerverdiAvgift.meldingskategori + SkattegrunnagOgBeregnetSkatt.skattleggingsperiode + Innsending.regnskapssystemreferanse |
| MvaSpesifikasjonslinje         | mvaKode + spesifikasjon + sats                                                                                                                                                |

The rules for SAF-t codes applies to the VAT return in the same manner as for SAF-T. The documentation for the rules may be found at https://www.skatteetaten.no/globalassets/bedrift-og-organisasjon/starte-og-drive/rutiner-regnskap-og-kassasystem/saf-t-regnskap/norwegian-saf-t-standard-vat-codes.pdf,

Rules for the VAT return

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
- Outbound VAT to be paid and inbound VAT to be deducted must be given as positive numbers in the VAT return

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
| Spesifikasjon                          | Specification                                         |

Test cases may be found in the [Test page](/english/test/)
