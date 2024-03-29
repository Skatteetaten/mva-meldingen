---
icon: "cloud"
title: "Questions and answers"
description: "Frequently asked questions"
---

[Norwegian](https://skatteetaten.github.io/mva-meldingen/kompensasjon/faq/)

## General

### New tax return for VAT compensation

The goal of the project was to achieve increased compliance, equal competitive conditions, simplification for reporting businesses, and a more effective administration of the VAT system.

#### When was the new tax return for VAT compensation launched?

The new tax return for VAT compensation was launched on January 1st 2023. The first deadline was April 10th 2023. Reports and corrections for terms up till and including December 31st 2022 must be submitted in the old format through Altinn, as before.

### Will there be a transition period from the old to the new services?

For the tax return for VAT compensation, there was no transition period.

### Will there be an "emergency" solution in case of technical difficulties?

For the tax return for VAT compensation, it is possible to file and submit the VAT-return in the online portal at skatteetaten.no.

### Who can fill out the tax return for VAT compensation, and who can submit?

To fill out and submit tax return for VAT compensation, these Altinn-roles are needed:
* 
* Fill out:
- Responsible auditor/Ansvarlig revisor
- Accounting employee/Regnskapsmedarbeider
- Accountant without signing rights/Regnskapsfører uten signeringsrettighet
- Assistant auditor/Revisormedarbeider


* Submit: 
- Limited signing rights/Begrenset signeringsrettighet
- Accountant with signing rights/Regnskapsfører med signeringsrettighet


* Attestation: 
- Responsible auditor/Ansvarlig revisor
- Auditor certifies validity of VAT compensation/Revisorattesterer - MVA Kompensasjon

### How will the new tax return for VAT compensation be submitted?

Businesses and advisors are encouraged to deliver directly from their ERP. For those who do not have an ERP, or if the ERP is not suited to deliver the tax return for VAT compensation, the Tax administration has a web-based portal for submitting tax return for VAT compensation. Altinn will still be used for identification and information exchange.

### Has a draft been made visually of what the new report should look like in the ERP?

The tax authorities do not set requirements for how the report looks in the accounting system. The goal is for users to keep accounts as normal, and for the system to compile the information from the accounts to the tax return for VAT compensation, so that the user can submit the return.
The new reporting is code-based and facilitates digital collaboration. Numbered fields are replaced by a dynamic list of specification lines. It is also possible to provide comments both for the entire report and per line. The code list for the tax return for VAT compensation is available on [Github](https://skatteetaten.github.io/mva-meldingen/kompensasjon_eng/informasjonsmodell/#encoding).

### Is it possible to attach files with documentation in the new tax return for VAT compensation?

Yes, it is possible to attach up to 50 files, and the files can be up to 25mb per file.
We will support the following file formats:

    - PDF
    - Open Office XML (OOXML)
    - Open Document Format (ODF)
    - JPG eller PNG

### What authentication methods will be used for tax return for VAT compensation submissions?

Authentication is carried out with personal login in ID-porten for both system-to-system and portal submissions, not by password and username like today. ERPs must offer ID-porten login window for their users, so they can log in using electronic ID from ID-porten. To avoid unnecessary logins user will stay logged in for 8 hours.

We want to offer Maskinporten support for system-to-system submissions and we are currently looking into the legal and practical issues concerning Maskinporten. ID-porten will be used until further notice.

### Will there be a code list of descriptions for the various codes?

This can be found on [Github](https://skatteetaten.github.io/mva-meldingen/kompensasjon_eng/informasjonsmodell/#encoding).

### Should VAT codes be entered with K in the tax return for VAT compensation?

No, the codes should not be entered with K in the tax return for VAT compensation.

When delivering a tax return for VAT compensation from an ERP accounting system or in the logged-in solution, only a numerical code is used, without the letter K in front or behind. This is according to standard code list in the document "Norwegian SAF-T Standard - VAT/Tax codes".

In the document, the letter K is only used in the description of the codes, so that the reader can more easily see that the VAT code and accompanying text are relevant for compensation purposes.

## Test

### Will testing of the tax return for VAT compensation be open for everyone?

Information regarding testing is open to everyone on [Github](https://skatteetaten.github.io/mva-meldingen/kompensasjon_eng/test).
