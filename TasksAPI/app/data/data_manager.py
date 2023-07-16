import json
from typing import Dict



def get_users() -> list[Dict]:
    with open("./app/data/fake_db.json", "r") as data:
        return json.load(data)
    
def get_tasks() -> list[Dict]:
    return [task for user in get_users() for task in user.get("tasks", [])]


def write_data(_data) -> None:
    with open("./app/data/fake_db.json", "w") as data:
        return json.dump(_data, data, indent=4)


