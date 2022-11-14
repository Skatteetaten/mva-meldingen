import requests


def hent_instans_events(altinn_plattform_miljø, instance_id, altinn_token):
    url = f"{altinn_plattform_miljø}/storage/api/v1/instances/{instance_id}/events"
    header = {'Authorization': f'Bearer {altinn_token}', 'accept': 'application/json'}
    response = requests.request("GET", url, headers=header)

    return response.json()

