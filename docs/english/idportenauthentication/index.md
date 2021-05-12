---
icon: "cloud"
title: "ID-Porten & Authentication"
description: "How to authenticate with ID-Porten"
---

## Introduction

## Start using ID-porten

When starting testing it is possible to use the Norwegian Tax Administration ID-porten integration , however we recommend setting up your own integration, as the process is partially manual, and when using the service in production each user must have their own integration. Another advantage of starting the integration process early is that the integration can be tested in the test environment. ID-porten is owned by the Norwegian Digitalisation Agency (Digdir) and details on how to start using ID-porten is provided here: <a href="https://samarbeid.digdir.no/id-porten/id-porten/18" target="_blank">ID-Porten documentation</a>. When ordering access, please provide information that you would like to access the skattemeldings-API from Skatteetaten.

A customer relationship with DigDir provides access to their self-service solution, which in turn provides access to the administration of the customer's use of ID-Porten. In the self-service solution, the customer can generate a so-called client_id and define a callback url:

- client_id: is an automatically generated unique identifier for the service.
- callback url: The Uri that the client is allowed to go to after logging in. After a successful login in ID-Porten, this url will be called.
  If it takes too long to establish a customer relationship with DigDir, the end-user systems can use Skatteetaten's client_id in the meantime. For this test, Skatteetaten has created the following client_id that can be used by the end-user systems:

      - `client_id: 23cc2587-ea4e-4a5f-aa5c-dfce3d6c5f09`
      	  - Callback URL for this client_id is set to  http://localhost:12345/token  (If there are consumers who want other callback URLs it can be provided)

**Useful links:**

- The client is using the test environment in DigDir called "verifikasjon 2": <a href="https://samarbeid.difi.no/node/232" target="_blank">https://samarbeid.difi.no/node/232</a>
- OICD integration is described here: <a href="https://difi.github.io/felleslosninger/oidc_index.html" target="_blank">https://difi.github.io/felleslosninger/oidc_index.html</a>
- How to create a client in the self service solution: <a href="https://minside-samarbeid.difi.no/organization-home/services/service-admin#/" target="_blank">https://minside-samarbeid.difi.no/organization-home/services/service-admin#/</a>

## Login with ID-porten

ID-porten login can be implemented in all types of end-user systems

- Desktop applications
- Web applications

Under the condition that the application can open a URL in a web browser, where login is carried out, and also has to be able run a web-server receiving a web-request (in the form of a redirect from ID-porten after login) on the callback-url.

The client must do the following REST call towards ID-porten:

- Launch the system browser and make authorization calls against ID-porten. Read more about it here: <a href="https://difi.github.io/felleslosninger/oidc_protocol_authorize.html" target="_blank">https://difi.github.io/felleslosninger/oidc_protocol_authorize.html</a>
- The user is then sent to ID-porten for login. Existing test users for testing towards Skatteetaten's services today can be used.
- Set up a web server waiting for callback from the browser. After successful login ID-Porten is sent used to this web server. This web server must be set to listen to callback URLs http://localhost:12345/token (as according to previous section).
- Make a token request. Read more about it here: <a href="https://difi.github.io/felleslosninger/oidc_protocol_token.html" target="_blank">https://difi.github.io/felleslosninger/oidc_protocol_token.html</a>

The following test environment at ID-porten is used:

- /authorize endpoint: `https://oidc-ver2.difi.no/idporten-oidc-provider/authorize`
- /token endpoint: `https://oidc-ver2.difi.no/idporten-oidc-provider/token`

For details on which HTTP parameters must be sent in the call, see the file [log_in_idporten.py](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/test/Steg/log_in_idporten.py)
