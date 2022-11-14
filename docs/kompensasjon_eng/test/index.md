---
icon: "cloud"
title: "Test & Production"
description: "Test and production information"
---

[Norwegian](https://skatteetaten.github.io/mva-meldingen/kompensasjon/test/)

## Changelog

| Date       | Changes                                                           |
| :--------- |:------------------------------------------------------------------|
| 2022.06.30 | New page for tax return for VAT compensation                      |
| 2022.15.11 | Removed Jupyter notebook demo, added reference to Phyton script   |

## Testing requirements

System providers are responsible for carrying out tests themselves. Focus should be to verify that the validation and submission services work as expected. The implementation guide is the essential guide for getting the solution in place for system providers.

The project team will contribute with debugging, bug fixing, and following up of cases that are sent into the test environment.

The project team is available via Slack for technical clarifications and for direct contact with developers and test managers. The project team can also be reached via mva-modernisering@skatteetaten.no. Contact us here to receive access to Slack.

## The test environment and test data

System providers must have test environments which can make use of synthetic data

Connection to the test environment occurs through ID-porten and for the purpose of testing, Skatteetaten's ID-porten integration can be used. It is recommended that the providers order their own integration against ID-porten as soon as possible because the process is partly manual and can be time consuming. See more in [implementation guide section 3. ID-porten integration.](https://skatteetaten.github.io/mva-meldingen/english/implementationguide/#3-id-porten-integration)

The ERP system providers must find test users in Tenor test data search. The testdata are synthetic test users that should also be used to log into ID-porten and Altinn. These are the only test users that can be used to test the tax return for VAT compensation. Ordinary Digdir test users will not work for this purpose.[Here is a guide to how to use Tenor test data search](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/mvameldingen_eng/test/User_Guide_Tenor_testdata.pdf).

Skatteetaten's test environment will be available as long as it is needed, after the new tax return for VAT compensation is launched.

## Test planning

The project team will offer meetings with a focus on test planning and carrying out the tests. Here the agendae will cover, amongst other things, carrying out the tests, which scenarios should be tested and the test data.

## Summary of tests and moving into production

The system providers will, after the end of the test period and in advance of production, summarise their tests. The summary will show what has been tested, along with the status of the carried out tests, including a summary of bugs and inadequacies. The providers will, at Skatteetatens request, provide documentation on how the integration has been tested.

# Test application - Phyton script
A Phyton script has been written in order to test the appliaction manually. For more information, please visit:
[Test av applikasjon ved hjelp av Phyton script](https://skatteetaten.github.io/mva-meldingen/test_with_phyton_script/).

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
