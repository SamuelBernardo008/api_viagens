from typing import Optional
from pydantic import BaseModel, ConfigDict

class ServicoSchema(BaseModel):
    nome_servico: str
    id_classe_minima: int

    model_config = ConfigDict(from_attributes=True)

class ServicoUpdateSchema(BaseModel):
    nome_servico: Optional[str] = None
    id_classe_minima: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)