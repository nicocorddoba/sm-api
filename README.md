# 📦 sm-api — Farmacias de turno en Santa María

API REST desarrollada con **FastAPI** para gestionar y consultar qué farmacia está de turno en Santa María según la fecha. Pensada para integrarse en bots, automatizaciones o aplicaciones informativas.

## 🚀 Características principales

- 🕗 Determina la **farmacia de turno actual** usando lógica de horarios personalizada (de 08:00 a 08:00 hs del día siguiente).
- 📅 Permite **cargar turnos** fácilmente mediante un endpoint `POST`.
- 🧩 Desarrollada con **FastAPI**, usando **PostgreSQL**, **SQLAlchemy** y **Alembic**.
- 🐳 Contenedorizada con **Docker** para facilitar el despliegue.

---

## 🧪 Endpoints disponibles

### 🔸 `GET /farmacia-de-turno`
Retorna la farmacia que está de turno actualmente según la hora local (08:00 a 08:00 del día siguiente).

#### Ejemplo de respuesta
```json
{
  "id": 0,
  "id_farmacia": 0,
  "nombre_farmacia": "Farmacia Central",
  "direccion_farmacia": "Calle 123",
  "numero_farmacia": "012345678",
  "fecha": "2025-06-30"
}
```

---

### 🔸 `POST /farmacia-de-turno`

Carga un nuevo turno de farmacia en la base de datos.

#### 📥 Body esperado

```json
{
  "fecha": "2025-06-25",
  "nombre": "Farmacia Central",
  "direccion": "Calle Falsa 123",
  "telefono": "123456789"
}
```

#### 📤 Respuesta exitosa

```json
{
  "msg": "Turnos creados correctamente"
}
```

---

### 🧰 Requisitos

- Python 3.13+
- PostgreSQL
- Docker (opcional pero recomendado)
