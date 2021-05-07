---
icon: "cloud"
title: "API"
description: "API descriptions"
---

## VAT return Validation and Submission API

VAT returns to be sent to Skatteetaten from an end-user
system (SBS) should use these APIs:

1.  Skatteetaten VAT return Validation API
2.  Skatteetaten Altinn3 VAT-Return-Submission API

as described below.

## Overall process for Submission a VAT return

The overall process for submitting VAT return:

1.  Log in with ID-Porten

    - Login is personal for each end user

2.  Validate VAT return with Skatteetaten's
    validation service

    - Authentication with ID-Porten token

3.  Exchange ID-Porten token with Altinn3 token

    - The API call is described just below the sequence diagram

4.  Send VAT return to the Altinn3 App

    - Authentication with Altinn3 token

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

**URL** : `POST https://<env>/api/mva-melding/valider`

Where `<env>`is an environment-specific address
e.g.`mp-test.sits.no`

**Body** :

- According to XSD:<a href="https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/english/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9.xsd" target="_blank">Skattemeldingformerverdiavgift.v0.9</a>

**Example** : Submitting XML in invalid format

POST <a href="https://mp-test.sits.no/api/mva-melding/skattemeldingformerverdiavgift/valider" target="_blank">https://mp-test.sits.no/api/mva-melding/skattemeldingformerverdiavgift/valider </a>

Header: `Content-Type: application/xml`

With content (http body) that does not pass <a href="https://github.com/Skatteetaten/mva-meldingen/tree/master/docs/english/informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9.xsd" target="_blank">XSD</a> validation:

```xml
<?xml version='1.0' encoding='UTF-8'?>
    <mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v0.9">

    </mvaMeldingDto>
```

**Returns** :

status: 200
Content (body)

```xml
<valideringsresultat>
        <status>UGYLDIG_SKATTEMELDING</status>
        <valideringsfeil>
            <stiTilFeil>//innfiling</stiTilFeil>
            <valideringsDetaljer>
                <feilmelding>Mva meldingen må være på gyldig format og passere XML skjema valideringen</feilmelding>
                <alvorlighetsgrad>UGYLDIG_SKATTEMELDING</alvorlighetsgrad>
                <avvikKode>MvaMeldingsinnhold_Xml_SkjemaValideringsfeil</avvikKode>
                <informasjon>cvc-complex-type.2.4.b: The content of element 'mvaMeldingDto' is not complete. One of
                    '{"no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v0.8":innfiling}' is expected.
                </informasjon>
            </valideringsDetaljer>
        </valideringsfeil>
    </valideringsresultat>
```

## VAT return submission Process

Submission of VAT returns are done with the Skatteetaten
Altinn3 App Instance API. The Instance API is a generic Altinn Api and its detailed description can be found here <a href="https://docs.altinn.studio/teknologi/altinnstudio/altinn-api/app-api/instances/" target="_blank">Instance API</a>. In-depth knowledge of this API is not required as this documentation
covers the needed sequence for submitting VAT returns.

It is recommended to use the <a href="https://skd.apps.tt02.altinn.no/skd/mva-melding-innsending-etm2/swagger/index.html" target="_blank">swagger documentation</a> along with this API description.

In addition, there are running examples of VAT return submission that use Jupyter Notebook and Python here: <a href="https://skatteetaten.github.io/mva-meldingen/english/test/" target="_blank">Test</a>

The filing process is performed with a sequence of calls to the Instance API and is described in detail below the sequence diagram and it is as follows:

1.  Exchange ID-Porten token to Altinn-Token. This token is used with the Instance API.
2.  Create Instance (sequence diagram starts here)
3.  Upload 1 VAT return filing (MvaMeldingInnsending)
4.  Upload 1 VAT return (mvaMeldingDto)
5.  Upload 0 or more Attachments
6.  File VAT return

The Instance VAT Filing API is available at this URL:

```
instanceApiUrl = "https://skd.apps.tt02.altinn.no/skd/mva-melding-innfiling-etm2/instances"
```

In the following sequence diagram, the application URL will be hidden, so if `POST: /intances/` is written it is
implicitly `POST: instanceApiUrl`

![](Mva-Melding-Innsending-Sekvensdiagram-English.png)

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

### Create Instance

An instance is an object in altinn that follows the process and the data model defined by the application. Skatteetaten has a VAT-Return-Filing application which has a process with currently one
step for filing. The step is a combination of upload and confirm the VAT return.

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

#### Response

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

The rest of the requests in the sequence for the filing use
`instanceUrl`. This can be found from the response at the
creation of the instance. See the example of the response above.

`instanceUrl` could either be picked from
`selflinks.apps` or derived from
`instanceApiUrl/{partyId}/{instanceGuid}`, where
`{partyId}` and `{instanceGuid}` can be
found in the `id` field in the returned instance.

Example instanceUrl:
`https://skd.apps.tt02.altinn.no/skd/mva-melding-innfiling-etm2/instances/3949387/abba061g-3abb-4bab-bab8-c9abbaf1ed50/data/28abba46-dea8-4ab7-ba90-433abba906df`

### Upload VAT return filing

MvaMeldingInnsending is a data type for metadata for the VAT return filing.
The object to populate is created during the instantiation and can
be found in the instance object's `data` list and has
`"dataType": "no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v0.1"`.
Since this object already exists when uploading VAT return filing,
PUT is used to update the data element.

The model for VAT return filing can be found here:
<a href="../informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v0.1.xsd" target="_blank">no.skatteetaten.fastsetting.avgift.mva.mvameldinginnsending.v0.1.xsd</a>

Url to MvaMeldingInnsending has this structure:

```
vatReturnFilingUrl = {instanceApiUrl}/{partyId}/{instanceGuid}/data/{dataGuid}
```

where `{dataGuid}` is the ID of the data object of the
instance.

There are 2 ways to derive the `vatReturnFilingUrl` and
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
  - `vatReturnFilingUrl = {instanceDataAppUrl}`

You upload VAT return filing by using the data api for the instance:

```
PUT {vatReturnFilingUrl}
    HEADERS:
        "Authorization": "Bearer " + "{altinnToken}"
        "content-type": "text/xml"
```

```xml
Content:
    <?xml version="1.0" encoding="UTF-8"?>
    <mvameldinginnsending>
        ...
    </mvameldinginnsending>
```

Example of xml file for VAT return filing can be found under <a href="https://skatteetaten.github.io/mva-meldingen/english/test/" target="_blank">Test</a>.

### Upload VAT return

The model is found here:
<a href="../informasjonsmodell/xsd/no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9.xsd" target="_blank">no.skatteetaten.fastsetting.avgift.mva.skattemeldingformerverdiavgift.v0.9.xsd</a>

The URL for uploading the VAT return has this structure:

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
    <mvaMeldingDto xmlns="no:skatteetaten:fastsetting:avgift:mva:skattemeldingformerverdiavgift:v0.9">
        ...
    </mvaMeldingDto>
```

This call will upload the xml document to the instance.

### Upload Attachments

It is possible to upload from 0 to 57 attachments, with an individual
size of 25MB.

Url for uploading attachments has this structure:

```
{instanceUrl}/data?datatype=vedlegg
```

The following content types are allowed for attachments:

- text/xml
- application/pdf
- image/jpeg
- image/jpg
- image/png
- image/gif

Attachments are uploaded with the following request to the instance data api:

```JSON
POST {instanceUrl}/data?datatype=vedlegg
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

### Submit VAT return filing

This step uses the process api for the instance and the instance will go to the next step for VAT return filing in the application process. Currently, there is only
one step in the application process, so at the time of writing, this request will complete the filing.

To complete the filing, the following call is made to the process api for the instance:

```JSON
PUT {instanceUrl}/process/next
    HEADERS:
        "Authorization": "Bearer " + "{altinnToken}"
        "content-type": "application/json"
```

The filing is now complete and can be found in Altinn's message archive.
