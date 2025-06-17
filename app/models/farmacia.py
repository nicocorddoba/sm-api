from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base


# Base = declarative_base()

class Farmacia(Base):
    __tablename__ = "farmacias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable= False)
    telefono = Column(String, nullable=False)
    
    farmacia_turno = relationship("Turno", back_populates="farmacia_turno")