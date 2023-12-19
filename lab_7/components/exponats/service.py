import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["exponats"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["exponats"]


def update_one_by_id(id, teacher):
    db = json_service.get_database()

    for i, elem in enumerate(db["exponats"]):
        if elem["id"] == id:

            elem["name"] = teacher["name"]
            elem["directors_id"] = teacher["directors_id"]

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


def create_one(exponat):
    db = json_service.get_database()

    last_exponat_id = get_all()[-1]["id"]
    db["exponats"].append({"id": last_exponat_id + 1, **exponat})

    json_service.set_database(db)
