from pydantic import BaseModel, ConfigDict, Field


# Esquema para la respuesta de un articulo
class FarmaciaResponse(BaseModel):
    id: int
    nombre: str
    direccion: str
    telefono: str
    
    model_config = ConfigDict(from_attributes=True)

# Esquema para crear un nuevo articulo
class FarmaciaCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    direccion: str = Field(..., min_length=3, max_length=100)
    telefono: str = Field(..., min_length=3, max_length=20)