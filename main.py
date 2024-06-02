from fastapi import FastAPI, HTTPException
from typing import List
from models import (
    Doador, DoadorResp, Usuario, UsuarioResp,
    Triagem, TriagemResp, Coleta, ColetaResp,
)
 
from database import get_next_id, create_item, get_items, get_item, update_item, delete_item


app = FastAPI()


@app.post("/usuario/", response_model=UsuarioResp)
def create_user_endpoint(usuario: Usuario):
    if get_item("usuario", usuario.id):
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    usuario.id = get_next_id("usuario")
    create_item("usuario", usuario)
    return usuario


@app.get("/usuario/", response_model=List[UsuarioResp])
def get_users_endpoint():
    return get_items("usuario")


@app.get("/usuario/{usuario_id}", response_model=UsuarioResp)
def get_user_endpoint(usuario_id: int):
    usuario = get_item("usuario", usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="User not found")
    return usuario


@app.put("/usuario/{usuario_id}", response_model=UsuarioResp)
def update_user_endpoint(usuario_id: int, usuario: Usuario):
    if not get_item("usuario", usuario_id):
        raise HTTPException(status_code=404, detail="User not found")
    update_item("usuario", usuario_id, usuario)
    return usuario


@app.delete("/usuario/{usuario_id}")
def delete_user_endpoint(usuario_id: int):
    if not get_item("usuario", usuario_id):
        raise HTTPException(status_code=404, detail="User not found")
    delete_item("usuario", usuario_id)
    return {"detail": "User deleted"}


@app.post("/doador/", response_model=DoadorResp)
def create_donor_endpoint(doador: Doador):
    doador_id = get_next_id("doador")
    doador_dict = doador.model_dump()
    doador_dict['id'] = doador_id
    create_item("doador", doador_dict)
    return doador_dict


@app.get("/doador/", response_model=List[DoadorResp])
def get_donors_endpoint():
    return get_items("doador")


@app.get("/doador/{doador_id}", response_model=DoadorResp)
def get_donor_endpoint(doador_id: int):
    if not get_item("doador", doador_id):
        raise HTTPException(status_code=404, detail="Donor not found")
    return get_item("doador", doador_id)


@app.put("/doador/{doador_id}", response_model=DoadorResp)
def update_donor_endpoint(doador_id: int, doador: Doador):
    if not get_item("doador", doador_id):
        raise HTTPException(status_code=404, detail="Donor not found")
    update_item("doador", doador_id, doador)
    return doador


@app.delete("/doador/{doador_id}")
def delete_donor_endpoint(doador_id: int):
    print(doador_id)
    if not get_item("doador", doador_id):
        raise HTTPException(status_code=404, detail="Donor not found")
    delete_item("doador", doador_id)
    return {"detail": "Donor deleted"}


@app.post("/triagem/", response_model=TriagemResp)
def create_triagem_endpoint(triagem: Triagem):
    if not get_item("doador", triagem.donor_id):
        raise HTTPException(status_code=404, detail="Donor not found")
    triagem_id = get_next_id("triagem")
    triagem_dict = triagem.model_dump()
    triagem_dict['id'] = triagem_id
    create_item("triagem", triagem_dict)
    return triagem_dict


@app.get("/triagem/", response_model=List[TriagemResp])
def get_triagens_endpoint():
    return get_items("triagem")


@app.get("/triagem/{triagem_id}", response_model=TriagemResp)
def get_triagem_endpoint(triagem_id: int):
    triagem = get_item("triagem", triagem_id)
    if not triagem:
        raise HTTPException(status_code=404, detail="Screening not found")
    return triagem


@app.put("/triagem/{triagem_id}", response_model=TriagemResp)
def update_triagem_endpoint(triagem_id: int, triagem: Triagem):
    if not get_item("triagem", triagem_id):
        raise HTTPException(status_code=404, detail="Screening not found")
    update_item("triagem", triagem_id, triagem)
    return triagem


@app.delete("/triagem/{triagem_id}")
def delete_triagem_endpoint(triagem_id: int):
    if not get_item("triagem", triagem_id):
        raise HTTPException(status_code=404, detail="Screening not found")
    delete_item("triagem", triagem_id)
    return {"detail": "Screening deleted"}


@app.post("/coleta/", response_model=ColetaResp)
def create_coleta_endpoint(coleta: Coleta):
    if not get_item("doador", coleta.donor_id):
        raise HTTPException(status_code=404, detail="Donor not found")

    if not get_item("usuario", coleta.user_id):
        raise HTTPException(status_code=404, detail="User not found")

    if not get_item("triagem", coleta.triagem_id):
        raise HTTPException(status_code=404, detail="Screening not found")

    coleta_id = get_next_id("coleta")
    coleta_dict = coleta.model_dump()
    coleta_dict['id'] = coleta_id
    create_item("coleta", coleta_dict)
    return coleta_dict


@app.get("/coleta/", response_model=List[ColetaResp])
def get_coletas_endpoint():
    return get_items("coleta")


@app.get("/coleta/{coleta_id}", response_model=ColetaResp)
def get_coleta_endpoint(coleta_id: int):
    coleta = get_item("coleta", coleta_id)
    if not coleta:
        raise HTTPException(status_code=404, detail="Collection not found")
    return coleta


@app.put("/coleta/{coleta_id}", response_model=ColetaResp)
def update_coleta_endpoint(coleta_id: int, coleta: Coleta):
    if not get_item("coleta", coleta_id):
        raise HTTPException(status_code=404, detail="Collection not found")
    update_item("coleta", coleta_id, coleta)
    return coleta


@app.delete("/coleta/{coleta_id}")
def delete_coleta_endpoint(coleta_id: int):
    if not get_item("coleta", coleta_id):
        raise HTTPException(status_code=404, detail="Collection not found")
    delete_item("coleta", coleta_id)
    return {"detail": "Collection deleted"}



