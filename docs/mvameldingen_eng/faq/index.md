---
icon: "cloud"
title: "Questions and answers"
description: "Frequently asked questions"
---

[Norwegian](https://skatteetaten.github.io/mva-meldingen/mvameldingen/faq/)

## General

### Which changes are coming in the modernisation of the VAT-domain?

#### New registration solution for the Value Added Tax Register.

The Tax Administration has launched a new registration solution for the Value Added Tax Register. With the new service, processing time for most registration cases will be reduced from weeks to minutes. [The new service can be found at Skatteetaten.no](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register/).

#### New VAT-return

The goal of the project was to achieve increased compliance, equal competitive conditions, simplification for reporting businesses, and a more effective administration of the VAT system. The new VAT-return was launched on 1 January 2022.

### Will there be a transition period from the old to the new services?

Coordinated Register Notification part 2 is no longer available for changing or deleting an application after the second quarter of 2021.
For the VAT-return, there is no transition period.

### Will there be an "emergency" solution in case of technical difficulties?

For the registration solution, it is possible to submit an incomplete application after the first stages of the service.
For the VAT-return it is possible to file and submit the VAT-return in the online portal at skatteetaten.no.

## Who can fill out an application for registration, and who can submit?

### Information about roles in Altinn

[Read more about Altinn-roles here.](https://www.altinn.no/en/help/profile/roles-and-rights/)

### VAT-registration roles

To fill out a registration application, the following roles are needed:
The business itself can fill out the VAT-registration, or someone with the Altinn role Auditor in charge/Ansvarlig revisor, Accounting employee/Regnskapsmedarbeider, Accountant with signing rights/Regnskapsfører med signeringsrettighet, Accountant without signing rights/Regnskapsfører uten signeringsrettighet, or Assistant auditor/Revisormedarbeider.
If you are going to sign the registration application on behalf of others, you must have the Altinn role “Limited signing rights/Begrenset signeringsrettighet", alternatively "Contact person NUF/Kontaktperson NUF”, if you are registering a Norwegian registered foreign enterprise (NUF).

### Delegated access to registration service

Legal councel and other advisors can ask the business to delegate access to "Merverdiavgift Registreringstjeneste" in Altinn. Alternatively the legal councel can request access from the business, if a prior relationship exists. Access can be given to a person or another business (only businesses with a prior relationship with the reporting business in Altinn). Legal councel who wants personal access can submit either their personal identity number or their Altinn-username, as identification for the reporting business. Access is not time-limited, so the reporting business should remove the access if the legal councel or advisor no longer needs access.

It is also possible for legal councel to acquire Altinn-roles in reporting businesses. This must be done in co-operation with the business in question. The role title will only be visible for the one who delegates, and not in other systems, such as the Register of Legal Entities.

### VAT-return roles

To fill out and submit VAT-returns, these Altinn-roles are needed:

The business itself can fill out the VAT-return, or someone with the Altinn role Auditor in charge/Ansvarlig revisor, Accounting employee/Regnskapsmedarbeider, Accountant without signing rights/Regnskapsfører uten signeringsrettighet or Assistant auditor/Revisormedarbeider.

If you are going to sign VAT-returns on behalf of others, you must have the Altinn role “Limited signing rights/Begrenset signeringsrettighet", "Contact person NUF/Kontaktperson NUF”, if you are registering a Norwegian registered foreign enterprise (NUF) and Accountant with signing rights/Regnskapsfører med signeringsrettighet .

### Addititional functionality

The Tax Administration have plans to develop functionality for delegating power of attorney in individual cases where there is need to delegate to a proxy. There can be a need for this in different cases, such as application, complaints and control. This is additional functionality which will be developed at a later time.

## VAT-return

### When will the new VAT-return be launched?

The new VAT-return was launched on January 1st 2022. This means that you must submit VAT-returns for periods after January 1st 2022 in the new format, according to the deadlines in your VAT-term. VAT-returns and corrections for terms up till and including December 31st 2021 must be submitted in the old format through Altinn, as before.

### How will the new VAT-return be submitted?

Businesses and advisors are encouraged to deliver directly from their ERP. For those who do not have an ERP, or if the ERP is not suited to deliver VAT-returns, the Tax administration has a web-based portal for submitting VAT-returns. Altinn is still used for identification and information exchange.

### Is delivery from the web-based portal a permanent solution that is open to everyone (if you can not or do not want to use system-system)?

Yes, the portal is a permanent solution that is open to everyone.

### Is it possible to see the logged in solution for manual entry of VAT-report before submitting?

You can log in to [the test environment here](https://skatt-sbstest.sits.no/web/mva/) to test the logged in solution. To use the testenvironment you must have Tenor testdata, user guide for obtaining these can be found [here](https://skatteetaten.github.io/mva-meldingen/mvameldingen_eng/test/#the-test-environment-and-test-data).

### Is it be possible to upload the VAT-return in XML-format in the logged in solution at Skatteetaten.no?

Yes, it is possible. It is not possible to change numbers or remarks in the uploaded XML-file, but it will be possible to upload attachements. If there are errors or you want to change a submitted VAT-report, upload a new XML-file. 

### At what aggregation level are amounts to be entered in the new VAT-return?

Same level as before. 

### Is it possible to attach files with documentation in the new VAT-return?

Yes, it is possible to attach up to 50 files, and the files can be up to 25mb per file.
We will support the following file formats:

    - PDF
    - Open Office XML (OOXML)
    - Open Document Format (ODF)
    - JPG eller PNG

### What authentication methods will be used for VAT-return submissions?

Authentication is carried out with personal login in ID-porten for both system-to-system and portal submissions, not by password and username. ERPs must offer ID-porten login window for their users, so they can log in using electronic ID from ID-porten. To avoid unnecessary logins user will stay logged in for 8 hours.

We want to offer Maskinporten support for system-to-system VAT-returns and we are currently looking into the legal and practical issues concerning Maskinporten. ID-porten will be used until further notice.

### Will it still be possible to submit a "Supplementary return"?

Supplementary returns are no longer in use. If there are changes in the ERP that makes it necessary to correct a VAT-return, this can be done by submitting a replacement VAT-return, after correcting the accounts in the ERP. The last VAT-return submitted for a term will be valid.

### How can we report VAT from a closed accounting period when we cannot use a supplementary return?

There are two alternatives:

1. Reopen the period (eg 1st term) and post the new information in this period, before the period is closed again. This means that the SAF-T file that supports the last VAT-return (given audit where SAF-T file submission has been required) can be taken from this accounting period. The tax authorities recommend reporting in this manner if possible.

2. Register the transaction in a new period (for example 2nd term), if the ERP functionality allows sorting the transactions in the in the right period. The transactions must be possible to separate from the other transactions, and the chain of audit must be maintained. The SAF-T file that supports the last submitted VAT return for 1st term (in case of audit) must then also contain the later period in which the new transactions / dispositions are posted. This may lead to submitting two SAF-T files for two different periods, to include the entire basis for the corrected VAT-return.

SAF-T files should only be submitted when requested by the Tax Authority, for audit purposes.

### How should jointly registered companies report the VAT return?

The reporting entity must deliver the VAT-report from the accounting system or in the portal, on behalf of all the jointly registered entities.

### When you round decimals on the basis and on the amount of VAT, then you can get "deviations" when you check by multiplying the basis by VAT percentage. Will this affect the validation?

Yes, we consider this in the validation, and have added a tolerance of +/-1kr x then umber of lines in the VAT-report. A VAT-report with three lines will have a tolerance of +/- 10kr, while a VAT-report with fourteen lines will have a tolerance of +/- 14kr.

### Is there a code list of descriptions for the various codes?

This can be found on [Github](https://skatteetaten.github.io/mva-meldingen/mvameldingen_eng/informasjonsmodell/#encoding).

### Is there an overview of how the old VAT-codes translate into SAF-T VAT-codes?

Yes, it can be found [here](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/mvameldingen/faq/Speiling_poster_mva-melding_SAF-T_koder.pdf).

## Test

### Will testing of the new VAT-report be open for everyone?

Information regarding testing is open to everyone on [Github](https://skatteetaten.github.io/mva-meldingen/mvameldingen_eng/test/).
