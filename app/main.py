from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, time


# FROM APP
from app.models import Farmacia, Turno
from app.schemas import FarmaciaCreate, TurnoCreate, TurnoResponse
from app.db.base import get_db


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Logica Turnos
def crear_farmacia(db: Session, farmacia: FarmaciaCreate) -> Farmacia:
    nueva_farmacia = Farmacia(**farmacia.model_dump())
    db.add(nueva_farmacia)
    db.commit()
    db.refresh(nueva_farmacia)
    return nueva_farmacia

@app.post("/turno/add")
def crear_turno(turnos: list[TurnoCreate], db: Session = Depends(get_db)):
    for turno_data in turnos:
        # Crear Farmacia si no existe
        farmacia_schema = FarmaciaCreate(
            nombre=turno_data.nombre_farmacia,
            direccion=turno_data.direccion_farmacia,
            telefono=turno_data.numero_farmacia
        )
        farmacia = db.query(Farmacia).filter_by(nombre=farmacia_schema.nombre).first()
        if not farmacia:
            farmacia = crear_farmacia(db, farmacia_schema)
            print("ID de farmacia:", farmacia.id)
            

        nuevo_turno = Turno(
            fecha=turno_data.fecha,
            id_farmacia=farmacia.id
        )
        db.add(nuevo_turno)
    db.commit()
    # db.refresh(nuevo_turno)

    return {"msg": "Turnos creados correctamente"}

@app.get("/turno", response_model=TurnoResponse)
def get_turno(db: Session= Depends(get_db)):
    ahora = datetime.now()

    # Determinar si estamos antes o después de las 8:00 AM
    if ahora.time() < time(8, 0):
        fecha_turno = (ahora - timedelta(days=1)).date()
    else:
        fecha_turno = ahora.date()

    turno = db.query(Turno).filter(Turno.fecha == fecha_turno).first()

    if not turno:
        raise HTTPException(status_code=404, detail="No hay turno registrado para el horario actual")

    return turno