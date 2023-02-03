---
icon: "cloud"
title: "Test & Production"
description: "Test and production information"
---

[Norwegian](https://skatteetaten.github.io/mva-meldingen/omvendt/test/)

## Changelog

| Date       | Changes                                                             |
| :--------- | :------------------------------------------------------------------ |
| 2023.01.30 | New page for VAT return for reverse tax liability    |

## Testing requirements

System providers are responsible for carrying out tests themselves. Focus should be to verify that the validation and submission services work as expected. The implementation guide is the essential guide for getting the solution in place for system providers.

The project team will contribute with debugging, bug fixing, and following up of cases that are sent into the test environment.

The project team is available via Slack for technical clarifications and for direct contact with developers and test managers. The project team can also be reached via mva-modernisering@skatteetaten.no. Contact us here to receive access to Slack.

## The test environment and test data

System providers must have test environments which can make use of synthetic data

Connection to the test environment occurs through ID-porten and for the purpose of testing, Skatteetaten's ID-porten integration can be used. It is recommended that the providers order their own integration against ID-porten as soon as possible because the process is partly manual and can be time consuming. See more in [implementation guide section 3. ID-porten integration.](https://skatteetaten.github.io/mva-meldingen/english/implementationguide/#3-id-porten-integration)

The ERP system providers must find test users in Tenor test data search. The testdata are synthetic test users that should also be used to log into ID-porten and Altinn. These are the only test users that can be used to test the VAT return for reverse tax liability. Ordinary Digdir test users will not work for this purpose.[Here is a guide to how to use Tenor test data search](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/mvameldingen_eng/test/User_Guide_Tenor_testdata.pdf).

Skatteetaten's test environment will be available as long as it is needed, after the VAT return for reverse tax liability is launched.

## Test planning

From February 15th you can test:

- Validation of a VAT-report in the "omvendt_avgiftsplikt" category, a VAT return for reverse tax liability.
- Submit a VAT return for reverse tax liability directly from the ERP accounting system.

After the VAT return for reverse tax liability is submitted from the ERP accounting system the submitting business will get a receipt in Altinn (https://tt02.altinn.no/ in test). 

It will also possible to carry out a manual submission of the VAT return for reverse tax liability in the portal "Min merverdiavgift" on Skatteetaten.no. 

## Test planning - Roles



Altinn roles for the VAT-report for VAT compensation:

- You can fill out and submit the VAT return for reverse tax liabilitywith these roles:

  - Limited signing rights/Begrenset signeringsrettighet
  - Accountant with signing rights/Regnskapsfører med signeringsrettighet.

- You can fill out the VAT return for reverse tax liability with these roles:

  - Responsible auditor/Ansvarlig revisor
  - Accounting employee/Regnskapsmedarbeider
  - Accountant without signing rights/Regnskapsfører uten signeringsrettighet
  - Assistant auditor/Revisormedarbeider


## Summary of tests and moving into production

The system providers will, after the end of the test period and in advance of production, summarise their tests. The summary will show what has been tested, along with the status of the carried out tests, including a summary of bugs and inadequacies. The providers will, at Skatteetatens request, provide documentation on how the integration has been tested.

# Test application - Python script

A Python script has been written in order to test the appliaction manually. For more information, please visit:
[Test application with Python script](https://skatteetaten.github.io/mva-meldingen/test_with_python_script_eng/).

## Test environment

### Test URLS:

| Service                   | Url                                                                                 |
| :------------------------ | :---------------------------------------------------------------------------------- |
| Validation Service        | https://idporten-api-sbstest.sits.no/api/mva/grensesnittstoette/mva-melding/valider |
| Submission Service        | https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/                    |
| Instance API-url          | https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/instances           |
| ID-porten integration     | https://oidc-ver2.difi.no/idporten-oidc-provider/.well-known/openid-configuration   |
| Altinn token exchange uri | https://platform.tt02.altinn.no/authentication/api/v1/exchange/id-porten            |

## Production environment

The production environment is functionally equal to the test environment.

### Production URLS:

| Service                   | Url                                                                                 |
| :------------------------ | :---------------------------------------------------------------------------------- |
| Validation Service        | https://idporten.api.skatteetaten.no/api/mva/grensesnittstoette/mva-melding/valider |
| Submission Service        | https://skd.apps.altinn.no/skd/mva-melding-innsending-v1/                           |
| Instance API-url          | https://skd.apps.altinn.no/skd/mva-melding-innsending-v1/instances                  |
| ID-porten integration     | https://oidc.difi.no/idporten-oidc-provider/.well-known/openid-configuration        |
| Altinn token exchange uri | https://platform.altinn.no/authentication/api/v1/exchange/id-porten                 |
