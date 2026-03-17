from typing import Optional

from pydantic import BaseModel

class CombustivelSchema(BaseModel):
    descricao: str
    fator_carbono: float

    class config:
        from_attributes = True
        

class CombustivelUpdateSchema(BaseModel):
    descricao: Optional[str]
    fator_carbono: Optional[float]


    class config:
        from_attributes = True
