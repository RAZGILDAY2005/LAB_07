import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["workers"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["workers"]


def update_one_by_id(id, teacher):
    db = json_service.get_database()

    for i, elem in enumerate(db["workers"]):
        if elem["id"] == id:

            elem["name"] = teacher["name"]
            elem["contacts"] = teacher["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["exponats"]):
        if elem["id"] == id:

            candidate = db["exponats"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(workers):
    db = json_service.get_database()

    last_workers_id = get_all()[-1]["id"]
    db["workers"].append({"id": last_workers_id + 1, **workers})

    json_service.set_database(db)
