---
icon: "cloud"
title: "API"
description: "API descriptions"
---

# VAT return Validation and Submission API

## Changelog

| Dato       | Hva ble endret?                                                                  |
|:-----------| :------------------------------------------------------------------------------- |
| 2021.06.17 | Updated documentation for [feedback](#retrieve-feedback).                        |
| 2021.07.05 | Corrected the datatype for when uploading attachments.                           |
| 2021.08.03 | Changed the URL for validation to the correct value                              |
| 2021.11.04 | Updated URL for validation service                                               |
| 2021.11.08 | Updated validation error list                                                    |
| 2021.11.11 | Updated error messages when filing submission                                    |
| 2021.12.08 | Updated valid content type for binaerVedlegg                                     |
| 2022.06.30 | Changes in connection with the expansion of documentation for other return types |           |
| 2022.08.06 | Added new conflict error message for duplicate file names |

## Introduction

The APIs function for the following categories of tax return: VAT-return (RF-0002/0004), VAT-return for reverse liability (RF-0005) and tax return for VAT compensation (RF-0009). When these types of returns are submitted to the Tax Authority from an end-user system (SBS) these APIs should be used:

1.  Skatteetaten VAT return Validation API
2.  Skatteetaten Altinn3 VAT-Return-Submission API

In the API description the VAT-return is used as a collective term for the various types of returns. The APIs are described below.

## Overall process for Submission and validating VAT return

Submission of VAT-returns are done with the Skatteetaten
Altinn3 App Instance API. The Instance API is a generic Altinn Api and its detailed description can be found here <a href="https://docs.altinn.studio/teknologi/altinnstudio/altinn-api/app-api/instances/" target="_blank">Instance API</a>. In-depth knowledge of this API is not required as this documentation
covers the needed sequence for submitting VAT returns.

It is recommended to use the <a href="https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/swagger/index.html" target="_blank">swagger documentation</a> along with this API description.

In addition, there are a Python script examples of VAT return filing here: <a href="https://skatteetaten.github.io/mva-meldingen/mvameldingen_eng/test/" target="_blank">Test</a>

The submission process is performed with a sequence of calls to the Instance API and is described in detail below the sequence diagram, and it is as follows:

1. Authentication
   - Change ID-Porten token to Altinn token
2. Validation
3. Data filling towards Altinn3-App
   - Create instance towards Altinn3-App
   - Upload vat-return submission towards Altinn3-App
   - Upload vat-return towards Altinn3-App
   - Upload attachements towards Altinn3-App
4. Complete data filling towards Altinn3-App
5. Complete submission towards Altinn3-App
6. Retrieve feedback towards Altinn3-App

The Instance VAT Filing API is available at this URL:

```
instanceApiUrl = "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/instances"
```

In the following sequence diagram, the application URL will be hidden, so if `POST: /intances/` is written it is
implicitly `POST: instanceApiUrl`

![](Vat-Return-Submission-Sequence-Diagram.png)

## Authentication

### Change ID-Porten token to the Altinn token

To change ID-Porten token, make the following calls:

```JSON
GET `https://platform.tt02.altinn.no/authentication/api/v1/exchange/id-porten`
    HEADERS:
        "Authorization": "Bearer " + "{IDPortenToken}"
           "content-type": "application/json"
```

and the response content will be a brand new altinnToken used as the
Bearer token in the subsequent requests. The token currently has a duration of 8 hours. Later in 2021, Altinn3 will offer refresh tokens so that one login can last for up to 3 months.

## Validate tax return

The service validates the content of a tax return and returns a response
with any errors, deviations and warnings. The service will do the
following:

1.  Check the message format.
2.  Control the content and composition of the elements in the VAT
    return.

Skatteetaten assumes that the validation service is called in
advance of submitting the VAT return. This ensures that the VAT return
has the correct format, content and increases the probability that
the VAT return will be approved upon submission.

**URL** : `POST https://<env>/api/mva/grensesnittstoette/mva-melding/valider`

Where `<env>`is an environment-specific address
e.g.`idporten-api-sbstest.sits.no`

**Body** :

- According to XSD:<a href="https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/informasjonsmodell_filer/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd" target="_blank">Skattemeldingformerverdiavgift.v1.0</a>

**Example** : Submitting XML in invalid format

POST https://idporten-api-sbstest.sits.no/api/mva/grensesnittstoette/mva-melding/valider

Header: `Content-Type: application/xml`

With content (http body) that does not pass <a href="https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/informasjonsmodell_filer/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd" target="_blank">XSD</a> validation:

```xml
<?xml version='1.0' encoding='UTF-8'?>
    <mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v1.0">

    </mvaMeldingDto>
```

### Response

status: 200
Content (body)

```xml
<valideringsresultat>
        <status>UGYLDIG_SKATTEMELDING</status>
        <valideringsfeil>
            <stiTilFeil>//innsending</stiTilFeil>
            <valideringsDetaljer>
                <feilmelding>Mva meldingen må være på gyldig format og passere XML skjema valideringen</feilmelding>
                <alvorlighetsgrad>UGYLDIG_SKATTEMELDING</alvorlighetsgrad>
                <avvikKode>MvaMeldingsinnhold_Xml_SkjemaValideringsfeil</avvikKode>
                <informasjon>cvc-complex-type.2.4.b: The content of element 'mvaMeldingDto' is not complete. One of
                    '{"no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v1.0":innsending}' is expected.
                </informasjon>
            </valideringsDetaljer>
        </valideringsfeil>
    </valideringsresultat>
```

## Create Instance

An instance is an object in altinn that follows the process and the data model defined by the application. Skatteetaten has a VAT-Return-Submission application which has a process with currently three
steps for submitting. The steps are uploading data, confirm and feedback.

In addition to being an object, an instance has a data object defined by a data model in the app.

Once an instance is created, it will be possible to update the data
object of the instance and add other data objects to the app's data
model. This is done in the next step.

To create an instance, you perform a POST request at the instanceApiUrl with an
`instanceOwner` object where you enter the organization
number for the organization that a VAT return is to be sent on behalf of:

```JSON
POST {instanceApiUrl}
    HEADERS:
        "Authorization": "Bearer " + "{altinnToken}"
        "content-type": "application/json"
    CONTENT/BODY:
        {
            "instanceOwner": {
                "organisationNumber": "{organizationNumber}"
                }
        }
```

This request will create the instance and return the following response

### Response

```JSON
Response HTTPCode: 201 (OK)
    Content:
    {
        "id": "{partyId}/{instanceGuid}",
        "instanceOwner": {
            "partyId": "{partyId}",
            "organisationNumber": "{organizationNumber}"
        },
        "appId": "skd/{ApplicationName}",
        "org": "skd",
        "selfLinks": {
            "apps": "{instanceUrl}", // the instanceUrl for the app
            "platform": "{platformUrl}" // the altinn3 plattform url for the instance
        },
        "data": [
            {
                "id": "{dataGuid}", // {dataGuid} can be used in the next step
                "instanceGuid": "{instanceGuid}",
                "dataType": "no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v0.1",
                "contentType": "application/xml",
                "blobStoragePath": "skd/{ApplicationName}/{instanceGuid}/data/{dataGuid}",
                "selfLinks": {
                    "apps": "{instanceDataAppUrl}", // {instanceDataAppUrl} can be used in the next step
                    "platform": "{instanceDataPlatformUrl}"
                },
                "size": 273,
                "locked": false,
                "refs": [],
                "isRead": true,
                "created": "2021-03-01T08:15:25.1139057Z",
                "createdBy": "86257",
                "lastChanged": "2021-03-01T08:15:25.1139057Z",
                "lastChangedBy": "86257"
            }
        ]
        // the rest of the object is snipped for documentation purposes
    }
```

The rest of the requests in the sequence for the submission use
`instanceUrl`. This can be found from the response at the
creation of the instance. See the example of the response above.

`instanceUrl` could either be picked from
`selflinks.apps` or derived from
`instanceApiUrl/{partyId}/{instanceGuid}`, where
`{partyId}` and `{instanceGuid}` can be
found in the `id` field in the returned instance.

Example instanceUrl:
`https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/instances/3949387/abba061g-3abb-4bab-bab8-c9abbaf1ed50/data/28abba46-dea8-4ab7-ba90-433abba906df`

### Error messages

_Response 400 - Bad Request:_ <br>

_Response 403 - Forbidden:_ <br>
Example Value:

```JSON
{"type":"https://tools.ietf.org/html/rfc7231#section-6.5.3","title":"Forbidden","status":403,"traceId":"00-44eab35cb9ca2049b24de316f380a774-a724e045b09dfc44-00"}
```

This error message could occur if you try to create an instance where the logged-in user does not have the necessary rights to the organisation number defined in the request header.
This can also occur if the user does not have the correct roles necessary for creating an instance.

_Response 404 - Not Found:_ <br>
Example Value:

```JSON
"Cannot lookup party: Failed to lookup party by organisationNumber: 123456789. The exception was: 404 - Not Found - "
```

This error message can occur when you set an invalid organisation number in the request header.

## Upload VAT return submission

MvaMeldingInnsending is a data type for metadata for the VAT return submission.
The object to populate is created during the instantiation and can
be found in the instance object's `data` list and has
`"dataType": "no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v0.1"`.
Since this object already exists when uploading VAT return submission,
PUT is used to update the data element.

The model for VAT return submission can be found here:
<a href="https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/xsd/no.skatteetaten.fastsetting.avgift.mvamvameldinginnsending.v1.0.xsd" target="_blank">no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v1.0.xsd</a>

Url to MvaMeldingInnsending has this structure:

```
vatReturnSubmissionUrl = {instanceApiUrl}/{partyId}/{instanceGuid}/data/{dataGuid}
```

where `{dataGuid}` is the ID of the data object of the
instance.

There are 2 ways to derive the `vatReturnSubmissionUrl` and
both use the instance's data list element that has the data type
`no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v0.1`.
When the instance is created, there is only one element in the list.

From the data element you can either:

- merge `{dataGuid}` that exists as value in
  `"id"` in the structure above,
  - alternatively use `{instanceApiUrl}/data/{dataGuid}`
- or use the `selfLinks.apps` value
  `{instanceDataAppUrl}`, as shown in the instance
  response in the previous step.
  - `vatReturnSubmissionUrl = {instanceDataAppUrl}`

You upload VAT return submission by using the data api for the instance:

```
PUT {vatReturnSubmissionUrl}
    HEADERS:
        "Authorization": "Bearer " + "{altinnToken}"
        "content-type": "application/xml"
```

```xml
Content:
    <?xml version="1.0" encoding="UTF-8"?>
    <mvameldinginnsending>
        ...
    </mvameldinginnsending>
```

Example of xml file for VAT return submission can be found under https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/informasjonsmodell_filer/example_files/konvolutt.

### Error Messages

_Response 403 - Forbidden:_ <br>
If the logged-in user attempt to upload a file to the instance, but the person does not have the correct roles, you will get the response code 403 in return.

## Upload VAT return

The model is found here:https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd


The URL for uploading the VAT return has this structure:

### Error Messages

_Response 403 - Forbidden:_ <br>
If the logged-in user attempt to upload a file to the instance, but the person does not have the correct roles, you will get the response code 403 in return.

```
{instanceUrl}/data?datatype=mvamelding
```

The VAT return is uploaded with the following request to the instance data api:

```JSON
POST {instanceUrl}/data?datatype=mvamelding
    HEADERS:
        "Authorization": "Bearer " + "{altinnToken}"
        "content-type": "text/xml"
        "Content-Disposition": "attachment; filename=mvaMelding.xml"
```

```xml
Content:
    <?xml version="1.0" encoding="UTF-8"?>
    <mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v1.0">
        ...
    </mvaMeldingDto>
```

This call will upload the xml document to the instance.

## Upload Attachments

It is possible to upload from 0 to 57 attachments, with an individual
size of 25MB.

Url for uploading attachments has this structure:

```
{instanceUrl}/data?datatype=binaerVedlegg
```

The following content types are allowed for attachments:

- text/xml
- application/pdf
- application/vnd.oasis.opendocument.formula
- application/vnd.oasis.opendocument.text
- application/vnd.oasis.opendocument.spreadsheet
- application/vnd.oasis.opendocument.presentation
- application/vnd.oasis.opendocument.graphics
- application/vnd.openxmlformats-officedocument.wordprocessingml.document
- application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
- application/vnd.openxmlformats-officedocument.presentationml.presentation
- application/msword
- application/vnd.ms-excel
- application/vnd.ms-powerpoint
- image/jpeg
- image/png

Attachments are uploaded with the following request to the instance data api:

```JSON
POST {instanceUrl}/data?datatype=binaerVedlegg
    HEADERS:
        "Authorization": "Bearer " + "{altinnToken}"
        "content-type": "application/pdf"
        "Content-Disposition": "attachment; filename=merknaderTilMvaMeldingen.pdf"
    Content:
    {pdf-attachment in binary format}
```

This request will upload the pdf document to the instance.

Remember that `content-type` should be appropriate for
the attachment to be uploaded and that the file name in the
`Content-Disposition` header should be appropriate
and unique. This is the file name Skatteetaten will refer to
for the attachment.

### Error Messages

_Response 403 - Forbidden:_ <br>
If the logged-in user attempt to upload a file to the instance, but the person does not have the correct roles, you will get the response code 403 in return.

## Complete Data Filling

This step uses the process api for the instance and the instance will go to the next step for VAT return filing in the application process.

To complete the data filling, the following call is made to the process api for the instance:

```JSON
PUT {instanceUrl}/process/next
    HEADERS:
        "Authorization": "Bearer " + "{altinnToken}"
        "content-type": "application/json"
```

The submission will now be in the confirmation step.

### Error Messages

_Response 403 - Forbidden:_ <br>
If the logged-in user attempt to update to the next task in the instance process, but does not have the correct roles, you will get the response code 403 in return.

_Response 409 - Conflict:_ <br>

```
"Valideringsfeil: Organisasjonsnummeret i instansen er forskjellig fra organisasjonsnummeret i MvaMeldingInnsending (\"konvolutt\")"
```

You will get this error message if the organisation number used when creating the instance is different from the organisation number defined in vat-return submission.

```
"Valideringsfeil: Organisasjonsnummeret i MvaMeldingInnsending (\"konvolutt\") er forskjellig fra organisasjonsnummeret i {filnavn}"
```

If the list of attachments defined in at-return submission is different from the attachments uploaded to the instance, you will get this error message.

```
"Valideringsfeil: Meldingskategorien i MvaMeldingInnsending (\"konvolutt\") er forsjellig fra Meldingskategorien i {filnavn}"
```

This error message will occur if the value of the field message category in vat-return submission is different from the message category in the vat-return.

```
"Valideringsfeil: skattleggingsperiode er påkrevd i MvaMeldingInnsending. Validation error: skattleggingsperiode is required in MvaMeldingInnsending"
```

This error message will occur if the value of the field skattleggingsperiode is null.

```
"Valideringsfeil: skattleggingsperiode må være utfylt. Validation error: skattleggingsperiode must be populated"
```

This error message will occur if the value of the field skattleggingsperiode is empty.

```
"Valideringsfeil: instansstatus er påkrevd i MvaMeldingInnsending. Validation error: instansstatus is required in MvaMeldingInnsending"
```

This error message will occur if the value of the field instansstatus is null.

```
"Valideringsfeil: filnavnene i innsendingen må være unike. Validation error: file names in the submission must be unique."
```

This error message will occur if two or more uploaded files have the same name.

**Validation Service**

```
"Valideringsfeil: Ugyldig mva-melding"
```

The app will also call the validation service during the completion of the data filling step. If the vat-return is invalid,
it will return a 409 error message, and the validation result in xml as content.

Example value:

```XML
<valideringsresultat>
    <status>UGYLDIG_SKATTEMELDING</status>
    <valideringsfeil>
        <stiTilFeil>//innsending</stiTilFeil>
        <valideringsDetaljer>
            <feilmelding>Mva meldingen må være på gyldig format og passere XML skjema valideringen</feilmelding>
            <alvorlighetsgrad>UGYLDIG_SKATTEMELDING</alvorlighetsgrad>
            <avvikKode>MvaMeldingsinnhold_Xml_SkjemaValideringsfeil</avvikKode>
            <informasjon>cvc-complex-type.2.4.b: The content of element 'mvaMeldingDto' is not complete. One of
                '{"no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v1.0":innsending}' is expected.
            </informasjon>
        </valideringsDetaljer>
    </valideringsfeil>
</valideringsresultat>
```

You can find an explanation for all the validation rules for respectively [VAT report](/mvameldingen_eng/forretningsregler/) and [Compensation report VAT](/kompensasjon_eng/forretningsregler/).

**Validation of MvaMeldingInnsending against the xsd model**
<a href="https://github.com/Skatteetaten/mva-meldingen/blob/master/docs/informasjonsmodell_filer/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd" target="_blank">no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v1.0.xsd</a>

Example:

```
Valideringsfeil / Validation error:
The 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0:skattleggingsperiodeToMaaneder' element is invalid - The value 'juli-september' is invalid according to its datatype 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0:SkattleggingsperiodeToMaaneder' - The Enumeration constraint failed.
The element 'mvaMeldingInnsending' in namespace 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0' has invalid child element 'opprettingstidspunkt' in namespace 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0'. List of possible elements expected: 'opprettetAv' in namespace 'no:skatteetaten:fastsetting:avgift:mva:mvameldinginnsending:v1.0'.
```

## Complete vat-return submission

This step uses the process-api for the instance, and it will end the confirmation step for the submission.
It will also update the instance to the next step in the application, the feedback step.

To complete the submission, the following call is used towards the process-api on the instance:

```JSON
PUT {instansUrl}/process/next
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "content-type": "application/json"
```

The submission will now be in the feedback step.

### Error Messages

_Response 403 - Forbidden:_ <br>
If the logged-in user attempt to update to the next task in the instance process, but does not have the correct roles, you will get the response code 403 in return.

_Response 409 - Conflict:_ <br>

```
"Valideringsfeil: filnavnene i innsendingen må være unike. Validation error: file names in the submission must be unique."
```

This error message will occur if two or more uploaded files have the same name. Unlikely during this step.

### Payment information available

When the submission is completed and the instance is in the feedback step, the payment information will be available for download. It can be found by downloading the instance and downloading the file `betalingsinformasjon.xml`, and has the data type `payment information`. See [feedback files](#feedback-files).

## Retrieve feedback

The Tax Administration has created 2 api-endpoints to simplify the development of this step:

- An endpoint, which returns a status on whether the Tax Administration has provided feedback.
- A synchronous endpoint, which returns the instance when the Tax Administration has processed the vat-return, and provided feedback.

The following sequence diagram shows how to identify if the Tax Administration has provided feedback to a given instance,
and how to retrieve it.
![](Get-Feedback.png)

You can get the status of the feedback by performing a request towards the feedback-api for the instance.

```JSON
GET {instansUrl}/{partyId}/{instanceGuid}/feedback/status
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "accept": "application/json"
```

If the call is successful it will return a status code 200, and a json object:

```JSON
{
  "isFeedbackProvided":	boolean
}
```

Where `isFeedbackProvided` returns as `true` if feedback has been given, otherwise it will return `false`

To retrieve the instance where the feedback has been provided, use a call towards the synchronous API-endpoint:

```JSON
GET {instansUrl}/{partyId}/{instanceGuid}/feedback
HEADERS:
    "Authorization": "Bearer " + "{altinnToken}"
    "accept": "application/json"
```

This endpoint will return the instance when the Tax Administration has given feedback,
and it will contain data elements for all the feedback files from the Tax Administration.

**Note: Latter mentioned endpoint should only be used in the following situations:**

- End user is waiting on feedback.
- After the status-endpoint has returned `isFeedbackProvided : true`

### Error Messages

_Response 400 - Bad Request:_ <br>
_Response 403 - Forbidden:_ <br>
This error message will occur if the logged-in user attempt to retrieve the instance, but the person does not have the correct roles.

_Response 404 - Not Found:_ <br>

### Feedback files

Once the Tax Administration has given feedback, the files for the feedback can be downloaded from the instance.

Payment information will be available when the submission is completed, it is being produced when [completing the vat return submission](#complete-vat-return-submission).

Example of feedback files given for a submission on the 17.06.2021 <a href = "https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/informasjonsmodell_filer/example_files/feedback/exampleSuccessfulFeedback17062021" target = "_ blank ">are located here </a>. These files were downloaded from an instance where the Tax Authorities had given feedback.

The files that can be downloaded will have `dataType`:

- betalingsinformasjon
- valideringsresultat
- kvittering

and download URLs are found in the instance object `data` elements returned from the feedback or instance api as shown below (irrelevant json removed).

Given a `data` element, the file can be retrieved using:

```JSON
GET {selfLinks.apps}
HEADERS:
    "Authorization": "Bearer" + "{altinnToken}"
```

where `selfLinks.apps` is retrieved from the list of data-elements on the instance as shown here:

```JSON
  "data": [
    {
      "id": "82c96a52-ad0b-428f-8005-7f214daf367e",
      "instanceGuid": "55604b08-1690-4a8d-bf6b-95c11dc40c58",
      "dataType": "valideringsresultat",
      "filename": "valideringsresultat.xml",
      "contentType": "text/xml",
      "selfLinks": {
        "apps": "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-sit/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/82c96a52-ad0b-428f-8005-7f214daf367e",
        "platform": "https://platform.tt02.altinn.no/storage/api/v1/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/82c96a52-ad0b-428f-8005-7f214daf367e"
      }
    },
    {
      "id": "726a315f-7e5e-4514-8ef1-5eda624407d4",
      "instanceGuid": "55604b08-1690-4a8d-bf6b-95c11dc40c58",
      "dataType": "betalingsinformasjon",
      "filename": "betalingsinformasjon.xml",
      "contentType": "text/xml",
      "selfLinks": {
        "apps": "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-sit/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/726a315f-7e5e-4514-8ef1-5eda624407d4",
        "platform": "https://platform.tt02.altinn.no/storage/api/v1/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/726a315f-7e5e-4514-8ef1-5eda624407d4"
      }
    },
    {
      "id": "cbce850a-a887-4598-aea4-710ea9ffdc7d",
      "instanceGuid": "55604b08-1690-4a8d-bf6b-95c11dc40c58",
      "dataType": "kvittering",
      "filename": "kvittering.pdf",
      "contentType": "application/pdf",
      "selfLinks": {
        "apps": "https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-sit/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/cbce850a-a887-4598-aea4-710ea9ffdc7d",
        "platform": "https://platform.tt02.altinn.no/storage/api/v1/instances/50267437/55604b08-1690-4a8d-bf6b-95c11dc40c58/data/cbce850a-a887-4598-aea4-710ea9ffdc7d"
      }
    }
  ]
```
