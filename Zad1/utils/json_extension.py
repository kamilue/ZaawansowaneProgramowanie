import json


def to_json_string(list_of_objects: list):
    obj = [o.__dict__() for o in list_of_objects]
    return json.dumps(obj, default=lambda obj: obj.__dict__)


def to_json(obj: str) -> any:
    return json.loads(obj)
