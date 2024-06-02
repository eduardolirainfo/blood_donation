from pydantic import BaseModel
from typing import List, Optional


class Doador(BaseModel):
    name: str
    age: int
    gender: str
    blood_type: str
    rh_factor: str
    health_conditions: List[str]
    contact_number: str
    address: str
    email: str
    user_id: int


class DoadorResp(Doador):
    id: int


class Usuario(BaseModel):
    username: str
    full_name: str
    email: str
    role: str


class UsuarioResp(Usuario):
    id: int


class Triagem(BaseModel):
    donor_id: int
    user_id: int
    date: str
    health_status: str
    comments: Optional[str] = None


class TriagemResp(Triagem):
    id: int


class Coleta(BaseModel):
    donor_id: int
    user_id: int
    date: str
    volume: float
    comments: Optional[str] = None


class ColetaResp(Coleta):
    id: int
