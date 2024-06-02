from fastapi.testclient import TestClient
from main import app
from tinydb import TinyDB, Query

client = TestClient(app)
db = TinyDB("teste.json", indent=4)


def test_create_user():
    response = client.post("/usuario/", json={"id": 1, "nome": "Fulano", "email": "invalid_email"})
    assert response.status_code == 422


def test_get_user():
    response = client.get("/usuario/1")
    assert response.status_code == 404


def test_update_user():
    response = client.put("/usuario/1", json={"nome": "Novo Nome"})
    assert response.status_code == 404


def test_delete_user():
    response = client.delete("/usuario/1")
    assert response.status_code == 404


def test_create_donor():
    response = client.post("/doador/", json={"id": 1, "nome": "Doador 1", "tipo_sanguineo": "A+"})
    assert response.status_code == 200


def test_get_donors():
    response = client.get("/doador/")
    assert response.status_code == 200


def test_get_donor():
    response = client.get("/doador/1")
    assert response.status_code == 200


def test_update_donor():
    response = client.put("/doador/1", json={"nome": "Novo Doador"})
    assert response.status_code == 200


def test_delete_donor():
    response = client.delete("/doador/1")
    assert response.status_code == 200


def test_create_triagem():
    response = client.post("/triagem/", json={"id": 1, "doador_id": 1, "resultado": "Apto"})
    assert response.status_code == 200


def test_get_triagens():
    response = client.get("/triagem/")
    assert response.status_code == 200


def test_get_triagem():
    response = client.get("/triagem/1")
    assert response.status_code == 200


def test_update_triagem():
    response = client.put("/triagem/1", json={"resultado": "Inapto"})
    assert response.status_code == 200


def test_delete_triagem():
    response = client.delete("/triagem/1")
    assert response.status_code == 200


def test_create_coleta():
    response = client.post("/coleta/", json={"id": 1, "doador_id": 1, "triagem_id": 1, "data_coleta": "2022-01-01"})
    assert response.status_code == 200


def test_get_coletas():
    response = client.get("/coleta/")
    assert response.status_code == 200


def test_get_coleta():
    response = client.get("/coleta/1")
    assert response.status_code == 200


def test_update_coleta():
    response = client.put("/coleta/1", json={"data_coleta": "2022-01-02"})
    assert response.status_code == 200


def test_delete_coleta():
    response = client.delete("/coleta/1")
    assert response.status_code == 200
