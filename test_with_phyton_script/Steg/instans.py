import requests
import polling
import os
from Steg.instans_dataelement import hent_dataelement


def opprett(altinn_app_miljø, altinn3_app, altinn_token, org_number):
    url = f"{altinn_app_miljø}/{altinn3_app}/instances/"
    header = {'Authorization': f'Bearer {altinn_token}', 'content-type': 'application/json'}
    payload = "{'instanceOwner': {'organisationNumber': " + org_number + "}}"

    response = requests.request("POST", url, headers=header, data=payload)

    if response.status_code == 201:
        print("Opprettelse av ny instans -- ok")
    else:
        print(response.status_code)
        print(response.content.decode('utf-8'))

    return response.json()


def neste_prosess(altinn_app_miljø, altinn3_app, instans_id, altinn_token, taskid=None):
    url = f"{altinn_app_miljø}/{altinn3_app}/instances/{instans_id}/process/next"
    if taskid is not None:
        url = f"{url}[?id={taskid}]"

    header = {'Authorization': f'Bearer {altinn_token}', 'content-type': 'application/json'}

    response = requests.request("PUT", url, headers=header)

    if response.status_code == 200:
        print("Oppdatering av instans prosess -- ok")
    else:
        print(response.status_code)
        print(response.content.decode('utf-8'))

    return response.json()


def hent_instans(altinn_app_miljø, altinn3_app, instans_id, altinn_token):
    url = f"{altinn_app_miljø}/{altinn3_app}/instances/{instans_id}/"
    header = {'Authorization': f'Bearer {altinn_token}'}

    response = requests.request("GET", url, headers=header)

    if response.status_code == 200:
        print("Henting av instans -- ok")
        print(response.content.decode('utf-8'))
    else:
        print(response.status_code)
        print(response.content.decode('utf-8'))

    return response.json()


def hent_tilbakemelding(altinn_app_miljø, altinn3_app, instans_id, altinn_token, path):
    url = f"{altinn_app_miljø}/{altinn3_app}/instances/{instans_id}/"
    header = {'Authorization': f'Bearer {altinn_token}'}
    tilbakemelding = polling.poll(
        lambda: __hent_tilbakemelding_status(url, header),
        check_success=lambda response: response['isFeedbackProvided'] is True,
        step=10,
        timeout=360)

    if tilbakemelding['isFeedbackProvided'] is True:
        instance = requests.request("GET", url, headers=header).json()
        data_element_list = instance['data']
        for dataElement in data_element_list:
            if dataElement['dataType'] == "kvittering" \
                    or dataElement['dataType'] == "betalingsinformasjon" \
                    or dataElement['dataType'] == "valideringsresultat":
                data_request = hent_dataelement(
                    altinn_app_miljø=altinn_app_miljø,
                    altinn3_app=altinn3_app,
                    instans_id=instans_id,
                    data_element_id=dataElement['id'],
                    altinn_token=altinn_token
                )

                if not os.path.exists(path):
                    os.makedirs(path)

                if dataElement['filename'] is None:
                    print(f"Klarte ikke å lagre ned dataelement={dataElement['id']}, filename var None")
                    break

                if dataElement['dataType'] == "kvittering":
                    data = data_request.content
                    file = open(path + dataElement['filename'], "wb+")
                else:
                    data = data_request.content.decode('utf-8')
                    file = open(path + dataElement['filename'], "w+")

                file.write(data)
                file.close()
                print("Lagret " + dataElement['filename'] + " til sti:", path)

        print("Hentet tilbakemeldings filer fra instans og lagret ned...")
    else:
        print("Klarte ikke å hente tilbakemeldingsfiler fra instansen")


def __hent_tilbakemelding_status(url, header):
    request = requests.request("GET", f"{url}/feedback/status", headers=header)

    return request.json()
