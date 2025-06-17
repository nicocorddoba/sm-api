from datetime import date
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


# Esquema para la respuesta de un articulo
class TurnoResponse(BaseModel):
    id: int
    id_farmacia: int
    nombre_farmacia: str
    direccion_farmacia: str
    numero_farmacia: str
    fecha: date
    
    model_config = ConfigDict(from_attributes=True)

# Esquema para crear un nuevo articulo
class TurnoCreate(BaseModel):
    # id_farmacia: Optional[int] = Field(..., min_length=3, max_length=50)
    nombre_farmacia:  str = Field(..., min_length=3, max_length=50)
    direccion_farmacia: Optional[str] = Field(..., min_length=3, max_length=50)
    numero_farmacia: Optional[str] = Field(..., min_length=3, max_length=50)
    fecha: date = Field(default=None)