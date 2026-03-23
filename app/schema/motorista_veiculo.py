from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class MotoristaVeiculoSchema(BaseModel):
    id_motorista: int
    id_veiculo: int
    datahora_inicio: Optional[datetime] = None 
    datahora_fim: Optional[datetime] = None
    

    class Config:
        from_attributes = True

class MotoristaVeiculoUpdateSchema(BaseModel):
    datahora_inicio: Optional[datetime]
    datahora_fim: Optional[datetime]

    class config:
        from_attributes = True