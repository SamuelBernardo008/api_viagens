from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    cpf: str
    data_nascimento: str
    idade: int
    senha: str
    email: str
    nome_usuario: str

    class config:
        from_attributes = True

class UsuarioUpdateSchema(BaseModel):
    cpf: Optional[str] = None
    data_nascimento: Optional[str] = None
    idade: Optional[int] = None
    senha: Optional[str] = None
    email: Optional[str] = None
    nome_usuario: Optional[str] = None

    class config:
        from_attributes = True