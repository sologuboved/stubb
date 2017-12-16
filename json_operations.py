import json


def dump_json(data, json_filename):
    with open(json_filename, 'w') as handler:
        json.dump(data, handler)


def load_json(json_filename):
    with open(json_filename) as data:
        return json.load(data)
