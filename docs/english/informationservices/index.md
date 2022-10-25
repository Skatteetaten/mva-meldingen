---
icon: "cloud"
title: "Information services"
description: "Description of the information services available through API"
---

# Information services (Innsyn) available from API

## Changelog

| Date       | Change                                |
| :--------- | :------------------------------------ |
| 2022.10.04 | Page for information services created |

# Maskinporten and Authentication
## Introduction
In order to authenticate with Maskinporten, some preparations must be made by the business that will make queries to the Tax Authority’s services

## Procedure for using Maskinporten
1\. Contact Digdir to gain access to Maskinporten. This can be done via Digdirs's collaboration portal (https://samarbeid.digdir.no/maskinporten/konsument/119)

2\. Create a user in Samarbeidsportalen. When the agreement with Digdir has been established and access is in place in Altinn, you can log in to Samarbeidsportalen. If it is the first time you as a consumer log in to Samarbeidsportalen, you must create a user in Samarbeidsportalen.

- Go to samarbeid.digdir.no
- Press "Min profil" in the top right corner.
- Press "Registrer deg" in the login window
- Register as a user with your work e-mail address
- Confirm the user by clicking on the link sent to the e-mail. (NB! Check your junk mail folder if the email does not appear in your inbox).

NB! Digdir has its own help pages that can be used for troubleshooting when no token is generated. If you still have problems, please contact Digdirs Servicedesk servicedesk@digdir.no.

3\. Get access to the scope
Access to the scope in Maskinporten is granted by the Tax Authority. The consumer can apply for access by the by sending an e-mail to mva-modernisering@skatteetaten.no with the organization number. The following scope have been created for the information services:
- skatteetaten:mvameldinginnsendingsstatus
 
When the Norwegian Tax Authority approves the application for access to the scope, the business can create tokens from the machine port for the specified scopes.

4\. Use the Tax Authority's api with a token from Maskinporten. To make calls to the api with a valid token, do the following:

1.	Make a call to Maskinporten to get a token that can be used in the Tax Authority's service. The procedure is described on Digdir's pages for how to use Maskinporten as a consumer:
2.	The token is added to the Authorization-header on all calls to the Tax Authority's service in the format: 'Authorization: Bearer'
3.	The tax authority verifies the token in Maskinporten, which guarantees that the provider has access to act on behalf of the specified consumer in the specified scope.
4.	Data is returned for the specified consumer

# MVA Innsyn API
## Introduction
The information services APIs can be used by end-user systems (ERPs) to obtain corresponding information offered via "Min Merverdiavgift".

## Request for information from the API
Use of the Innsyn APIs requires that the ERP is authenticated via Maskinporten and that delegation between the reporting business and the ERP is configured in Altinn.

Requests for information are made as HTTP GET calls to the Tax Authority's APIs and responses are returned in XML or JSON format. Which format is desired is specified in the "Accept" header in the HTTP request. Sequence of requests:

1. Authentication in Maskinporten.
2. Submit calls to the Tax Authority

![](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/innsynstjenester/Sekvensdiagram%20innsyn%20SBS.png)

## Status for submission of VAT return
The service provides status for the current term(s) and terms where the there are missing VAT-returns.

**URL** : GET https://<env>/api/mva/grensesnittstoette/innsyn/melding/innsending/status/v1/{organisasjonsnummer}
Where `<env>` is environment-specific address e.g. mp-test.sits.no

**Example** : Request for submission status for organization number 123456789

`GET https://mp-test.sits.no/api/mva/grensesnittstoette/innsyn/melding/innsending/status/v1/123456789`

Headers:
`Accept: application/xml`
`Authorization: Bearer <maskinportentoken>`
**Response**
`status: 200 Innhold (body)`
**Error messages**
_Respons 401 - Unauthorized:_
If the token from Maskinporten does not match the requested organization.

## Information model
Graphic representation of the xsd for the [information service](Informasjonsmodell mvaInnsendingStatus.PNG) :

![](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/innsynstjenester/InformasjonsmodellmvaInnsendingStatus.PNG)


Version 1.0 of the XSD for the response is located here: [no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd](https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/documentation/informasjonsmodell/xsd/no.skatteetaen.fastsetting.avgift.mva.mvaMeldingInnsendingStatus.v1.xsd)
