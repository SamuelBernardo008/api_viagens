from pydantic import BaseModel
from typing import Optional

class MetodoPagamentoSchema(BaseModel):
    descricao: str
    nome_financiera: str

    class Config:
        from_attributes = True

class MetodoPagamentoUpdateSchema(BaseModel):
    descricao: Optional[str] = None
    nome_financiera: Optional[str] = None