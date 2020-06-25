import json


class DataIntegrityError(Exception):
    pass


def save_user(data: dict,path:str):
    with open(path, 'r') as fd:
        saved_data = fd.read()

    data = filter_person_data(data)

    if not saved_data:
        data = [data]
    else:
        prev_data = json.loads(saved_data)
        prev_data.append(data)
        data = prev_data

    with open(path, 'w') as fd:
        json.dump(data, fd)


def filter_person_data(data: dict) -> dict:
    data_model = {
        'name': str,
        'surname': str,
        'age': str,
        'gender': str
    }
    filtered_data = {}
    for key, _type in data_model.items():
        if key not in data:
            raise DataIntegrityError(f'"{key}" field is required')
        filtered_data[key] = _type(data[key])
    return filtered_data


def search_user(keyword: str,path:str) -> list:
    with open(path, 'r') as fd:
        saved_data = fd.read()

    if not saved_data:
        return []

    persons = json.loads(saved_data)
    if keyword:
        return [person for person in persons
                if person['name'].lower() == keyword.lower() or person['surname'].lower() == keyword.lower()]
