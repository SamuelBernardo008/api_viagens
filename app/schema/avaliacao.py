from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AvaliacaoSchema(BaseModel):
    nota_passageiro: Optional[int] = None
    nota_motorista: Optional[int] = None
    datahora_limite: datetime

    class Config:
        from_attributes = True

class AvaliacaoUpdateSchema(BaseModel):
    nota_passageiro: Optional[int] = None
    nota_motorista: Optional[int] = None