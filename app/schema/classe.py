from typing import Optional

from pydantic import BaseModel

class ClasseSchema(BaseModel):
    nome_classe: str
    fator_preco: float

    class config:
        from_attributes = True
        

class ClasseUpdateSchema(BaseModel):
    nome_classe: Optional[str]
    fator_preco: Optional[float]


    class config:
        from_attributes = True
