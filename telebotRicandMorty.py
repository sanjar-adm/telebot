import requests


def get_character_data_by_name(name):
    response = requests.get(f"https://rickandmortyapi.com/api/character?name={name.lower()}")

    if response.status_code == 404:
        return None

    return response.json()['results'][0]