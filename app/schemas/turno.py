from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


# Esquema para la respuesta de un articulo
class TurnoResponse(BaseModel):
    id: int
    id_farmacia: int
    nombre_farmacia: str
    direccion_farmacia: str
    numero_farmacia: str
    fecha: datetime
    
    model_config = ConfigDict(from_attributes=True)

# Esquema para crear un nuevo articulo
class TurnoCreate(BaseModel):
    # id_farmacia: str = Field(..., min_length=3, max_length=50)
    nombre_farmacia:  str = Field(..., min_length=3, max_length=50)
    direccion_farmacia: str | None = Field(..., min_length=3, max_length=50)
    numero_farmacia: str | None = Field(..., min_length=3, max_length=50)
    fecha: datetime = Field(default=None)