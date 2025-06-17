from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.base import Base


# Base = declarative_base()

class Turno(Base):
    __tablename__ = "turno"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_farmacia = id_estado = Column(Integer, ForeignKey("farmacias.id"), nullable=False, index=True)
    fecha = Column(Date, nullable= False)
    
    farmacia_turno = relationship("Farmacia", back_populates="farmacia_turno")
    
    # Property for getting the pharmacy's name
    @property
    def nombre_farmacia(self) -> str:
        return self.farmacia_turno.nombre_farmacia
    
    @property
    def direccion_farmacia(self) -> str:
        return self.farmacia_turno.direccion
    
    @property
    def telefono_farmacia(self) -> str:
        return self.farmacia_turno.telefono
    