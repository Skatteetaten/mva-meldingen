import polling
import os
import requests
from Steg import get_instance


def get_feedback_async(instance_id, altinn_token, domene, app):
    instance = polling.poll(
        lambda: get_instance.get(domene + app + "/instances/" + instance_id, altinn_token),
        check_success=lambda response: response['status']['isArchived'] is True and (
                response['status']['substatus']['label'] == "Godkjent" or
                response['status']['substatus']['label'] == "Ugyldig"),
        step=10,
        timeout=360)

    return instance


def get_feedback_sync(instance_id, altinn_token, domene, app):
    header = {'Authorization': 'Bearer ' + altinn_token, 'accept': 'application/json'}
    request = requests.get(domene + app + "/instances/" + instance_id + "/feedback", headers=header)

    print("status code:", request.status_code)
    print("reason:", request.reason)
    print("headers:", request.headers)
    print("content:", request.content.decode("utf-8"), "\n")

    return request


def save_to_disk(instance, _altinn_token, path):
    data_element_list = instance['data']
    for dataElement in data_element_list:
        if dataElement['dataType'] == "kvittering" \
                or dataElement['dataType'] == "betalingsinformasjon" \
                or dataElement['dataType'] == "valideringsresultat":
            data_request = get_instance.get_data(dataElement['selfLinks']['apps'], _altinn_token)
            if not os.path.exists(path):
                os.makedirs(path)
            if dataElement['dataType'] == "kvittering":
                data = data_request.content
                file = open(path + dataElement['filename'], "wb+")
            else:
                data = data_request.content.decode('utf-8')
                file = open(path + dataElement['filename'], "w+")
            file.write(data)
            file.close()

            print("Saved " + dataElement['filename'] + " to path:", path)
