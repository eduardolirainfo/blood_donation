from tinydb import TinyDB, Query
from typing import TypeVar, List, Optional

# TypeVar para permitir tipos genéricos
T = TypeVar('T')


def get_next_id(model_name: str) -> int:
    db = TinyDB(model_name + '.json', indent=4)
    # Obtenha todos os itens do modelo
    items = db.all()
    if items:
        return max(item['id'] for item in items) + 1
    else:
        return 1


def create_item(model_name: str, item: T):
    db = TinyDB(model_name + '.json', indent=4)
    db.insert(item)


def get_items(model_name: str):
    mdbname = model_name + '.json'
    db = TinyDB(mdbname, indent=4)
    if not db.all():
        return []
    return db.all()


def get_item(model_name: str, item_id: int):
    mdbname = model_name + '.json'
    db = TinyDB(mdbname, indent=4)
    item = db.search(Query().id == item_id)
    if not item:
        return None
    return db.get(doc_id=item_id)


def update_item(model_name: str, item_id: int, item: T):
    db = TinyDB(model_name + '.json', indent=4)
    if not get_item(model_name, item_id):
        raise ValueError(f"{model_name} not found")
    db.update(item.dict(), doc_ids=[item_id])


def delete_item(model_name: str, item_id: int):
    db = TinyDB(model_name + '.json', indent=4)
    if not get_item(model_name, item_id):
        raise ValueError(f"{model_name} not found")
    db.remove(doc_ids=[item_id])
