# README — AVISTAR Backend

## AVISTAR API

Backend REST API para la plataforma AVISTAR, una aplicación full stack para gestionar hospedajes, casas y apartamentos.

La API fue desarrollada con FastAPI y PostgreSQL siguiendo una arquitectura REST separada del cliente.

---

# Repositorio del frontend

```txt
https://github.com/Adairvlz/frontend-avistar
```

# Tecnologías utilizadas

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- Swagger / OpenAPI
- Python 3.12

---

# Características implementadas

## CRUD completo

- GET `/series`
- GET `/series/{id}`
- POST `/series`
- PUT `/series/{id}`
- DELETE `/series/{id}`

## Features adicionales

- Paginación
- Búsqueda por nombre
- Ordenamiento
- Validaciones server-side
- Sistema de ratings
- Exportación CSV desde frontend
- Swagger UI
- Persistencia en PostgreSQL
- Manejo de errores HTTP
- Soporte para imágenes

---

# Estructura del proyecto

```txt
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
└── routes/
    ├── series.py
    └── ratings.py
```

---

# Backend en producción (Railway)

## URL del backend

```txt
backend-avistar-production.up.railway.app
```

## Swagger UI

```txt
backend-avistar-production.up.railway.app/docs
```

## Cómo desplegar en Railway

URL publica: https://adairvlz.github.io/frontend-avistar/

1. Subir el repositorio a GitHub.
2. Crear un proyecto en Railway.
3. Seleccionar "Deploy from GitHub Repo".
4. Agregar un servicio PostgreSQL.
5. Configurar la variable:

```env
DATABASE_URL=${{Postgres.DATABASE_URL}}
```

6. Railway detectará automáticamente el Dockerfile y realizará el deploy.

---

# Cómo correr el proyecto localmente

## Requisitos

- Docker Desktop
- Git

## 1. Clonar repositorio

```bash
git clone <https://github.com/Adairvlz/backend-avistar>
cd avistar-backend
```

## 2. Levantar contenedores

```bash
docker compose up --build
```

---

# Puertos utilizados

## Backend

```txt
http://localhost:8010
```

## Swagger UI

```txt
http://localhost:8010/docs
```

## PostgreSQL

```txt
localhost:5428
```

---

# Variables de entorno

Archivo `.env`

```env
DATABASE_URL=postgresql://avistar_user:avistar_password@db:5432/avistar_db
```

---

# ¿Qué es CORS?

CORS es una política de seguridad del navegador que bloquea peticiones entre distintos orígenes. En este proyecto se configuró FastAPI para permitir conexiones desde el frontend mediante `CORSMiddleware`.

---

# Docker

## Dockerfile

El backend corre dentro de un contenedor Docker usando Python 3.12.

## Docker Compose

Se utiliza Docker Compose para levantar:

- Backend FastAPI
- PostgreSQL

---

# Challenges implementados

- Swagger/OpenAPI
- Swagger UI
- Códigos HTTP correctos
- Validaciones server-side
- Paginación
- Búsqueda por nombre
- Ordenamiento ascendente y descendente
- Sistema de ratings
- Exportación CSV
- Persistencia real con PostgreSQL
- Frontend usando fetch() y JavaScript vanilla
- Dockerización del backend y frontend

---

# Screenshots

## Backend Swagger

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/c6465c95-9f3d-48db-9f22-170fb2a1d349" />


## Frontend funcionando

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/fe37959c-e804-4377-af35-073450071938" />
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/eb36b45b-fb31-48a2-bee1-25c6541fdf09" />

---

# Reflexión personal

Utilizando las tecnologias de FastAPI si senti una gran diferencia a la hora de programar ya que python facilita muchisimo el entender el codigo y en modificarlo, pero lo que mas me gusto fue el Swagger que ofrece el framework que es increiblemente facil de usar, mucho mas que postman porque te dan los ejemplos de como subir los datos y ahi podias ver de una vez que todo funcionara de una vez.

Si volveria a utilizar estas tecnologias, de hecho de todos los proyectos que habia hecho anteriormente, este fue el que mas se me facilito a la hora de corregir errores.

