from pydantic import BaseModel
from enum import Enum
from typing import Optional

class PropriedadeEnum(str, Enum):
    alugado = "alugado"
    proprio = "proprio"

class ModeloVeiculoSchema(BaseModel):
    nome_modelo: str
    cor: str
    fabricante: str
    ano: int
    capacidade: int
    propriedade: PropriedadeEnum
    id_combustivel: int

    class Config:
        from_attributes = True

class ModeloVeiculoUpdateSchema(BaseModel):
    nome_modelo: Optional[str]
    cor: Optional[str]
    fabricante: Optional[str]
    ano: Optional[int]
    capacidade: Optional[int]
    propriedade: Optional[PropriedadeEnum]
    
    class Config:
        from_attributes = True