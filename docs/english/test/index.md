---
icon: "cloud"
title: "Test"
description: "Test cases VAT-return and test plan"
---

## Testing requirements

System providers are responsible for carrying out tests themselves. Focus should be to verify that the validation and submission services work as expected. The implementation guide is the essential guide for getting the solution in place for system providers.

The project team will contribute with debugging, bug fixing, and following up of cases that are sent into the test environment.

The project team is available via Slack for technical clarifications and for direct contact with developers and test managers. The project team can also be reached via mva-modernisering@skatteetaten.no. Contact us here to receive access to Slack.

## The test environment and test data

System providers must have test environments which can make use of synthetic data

Connection against the test environment occurs through ID-porten and for the purpose of testing, Skatteetaten's ID-porten integration can be used. It is recommended that the providers order their own integration against ID-porten as soon as possible because the process is partly manual and can be time consuming. See more in [implementation guide section 3. ID-porten integration.](https://skatteetaten.github.io/mva-meldingen/english/implementationguide/#3-id-porten-integration)

The ERP system providers must contact the project at mva-modernisering@skatteetaten.no to receive test users. These are synthetic test users that should also be used to log into ID-porten and Altinn. These are the only test users that can be used to test VAT-return. Ordinary Digdir test users will not work for this purpose.

Skatteetaten's test environment will be available at agreed periods between May 2021 and January 2022. In July 2021 it should not be expected that the environment will be available.

## Test planning

The project team will offer meetings with a focus on test planning and carrying out the tests. Here the agendae will cover, amongst other things, carrying out the tests, which scenarios should be tested and the test data.

## Summary of tests and moving into production

The system providers will, after the end of the test period and in advance of production, summarise their tests. The summary will show what has been tested, along with the status of the carried out tests, including a summary of bugs and inadequacies. The providers will, at Skatteetatens request, provide documentation on how the integration has been tested.

## Test applications

Some test applications has been written in jupyter notebook, for use when testing the solution from the Tax adminisatration:

1. [Jupyter notebook demo for fetching and validation](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/demo.ipynb). Downlaod the catalog 'test' and run the script demo.ipynb (The script will carry out all steps in the process: call ping service to check connection and validate VAT-return).

2. [Jupyter notebook demo for fetching, validation and submission](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/file-vat-return.ipynb). run the script file-vat-return.ipynb. It will run all the steps in the process.

3. [Pyton script to fetch token](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/Steg/log_in_idporten.py) and [postman script to validate return](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/MeldingValidering.postman_collection.json). First log in to [ID-Porten](https://skatteetaten.github.io/mva-meldingen/english/idportenauthentication/), and save the token in the format "Bearer <em>hentet-token</em>" as the environment variablewith the name "test-bearer" in postman, and use the postman script to validate the return.

4. [Example XML's](https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/documentation/test/eksempler/melding)

## 'Test 4'

During week 19 will all of the documentation be updated and available here on github.

The test environment will be available from the 25th of May.

![Testplan](Testplan_eng.png)
