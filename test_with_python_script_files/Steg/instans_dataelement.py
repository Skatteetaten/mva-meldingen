import requests
import json


def hent_dataelement(altinn_app_miljø, altinn3_app, instans_id, data_element_id, altinn_token):
    url = f"{altinn_app_miljø}/{altinn3_app}/instances/{instans_id}/data/{data_element_id}"
    header = {'Authorization': f'Bearer {altinn_token}'}

    response = requests.request("GET", url, headers=header)

    if response.status_code == 200:
        print("Henting av instans data element -- ok")
    else:
        print(response.status_code)
        print(response.content.decode('utf-8'))

    return response.json()


def last_opp_vedlegg(altinn_app_miljø, altinn3_app, instans_id, altinn_token, content_type, filnavn, vedlegg):
    url = f"{altinn_app_miljø}/{altinn3_app}/instances/{instans_id}/data?dataType=binaerVedlegg"
    with open(f"./files/vedlegg/{vedlegg}", 'rb') as file:
        payload = file.read()
    file.close()
    header = {'Authorization': f'Bearer {altinn_token}', 'content-type': f'{content_type}',
              'Content-Disposition': f'attachment; filename={filnavn}'}

    response = requests.request("POST", url, headers=header, data=payload)

    if response.status_code == 201:
        print("Opplastning av vedlegg til instans -- ok")
    else:
        print(response.status_code)
        print(response.content.decode('utf-8'))

    return response.json()


def last_opp_miljoefil(altinn_app_miljø, altinn3_app, instans_id, altinn_token, miljo):
    url = f"{altinn_app_miljø}/{altinn3_app}/instances/{instans_id}/data?dataType=miljo"
    payload = json.dumps(miljo)
    header = {'Authorization': f'Bearer {altinn_token}', 'content-type': 'application/json',
              'Content-Disposition': 'attachment; filename=miljofil.json'}

    response = requests.request("POST", url, headers=header, data=payload)

    if response.status_code == 201:
        print("Opplastning av miljø fil til instans -- ok")
    else:
        print(response.status_code)
        print(response.content.decode('utf-8'))

    return response.json()


def last_opp_mva_melding(altinn_app_miljø, altinn3_app, instans_id, melding_xml, altinn_token):
    url = f"{altinn_app_miljø}/{altinn3_app}/instances/{instans_id}/data?dataType=mvamelding"
    payload = bytearray(melding_xml, 'utf-8')
    header = {'Authorization': f'Bearer {altinn_token}', 'content-type': 'text/xml',
              'Content-Disposition': 'attachment; filename=mva-melding.xml'}

    response = requests.request("POST", url, headers=header, data=payload)

    if response.status_code == 201:
        print("Opplastning av mva melding til instans -- ok")
    else:
        print(response.status_code)
        print(response.content.decode('utf-8'))

    return response.json()


def oppdater_konvolutt(altinn_app_miljø, altinn3_app, instans_id, data_element_id, konvolutt_xml, altinn_token):
    url = f"{altinn_app_miljø}/{altinn3_app}/instances/{instans_id}/data/{data_element_id}"
    payload = bytearray(konvolutt_xml, 'utf-8')
    header = {'Authorization': f'Bearer {altinn_token}', 'content-type': 'application/xml',
              'Content-Disposition': 'attachment; filename=konvolutt.xml'}

    response = requests.request("PUT", url, headers=header, data=payload)

    if response.status_code == 201:
        print("Oppdatering av mva konvolutt på instans -- ok")
    else:
        print(response.status_code)
        print(response.content.decode('utf-8'))

    return response.json()
