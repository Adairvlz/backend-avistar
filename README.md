# Avistar - Backend (FastAPI)

Este repositorio (o carpeta) contiene la API del proyecto **Avistar**, desarrollada con **FastAPI (Python)** y utilizando una base de datos **PostgreSQL**.

## 🚀 Requisitos Previos

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🛠️ Cómo Correr el Proyecto Completo

Para que la aplicación funcione en su totalidad, necesitas levantar los servicios del backend (API y Base de Datos) y luego ejecutar el frontend.

### 1. Configurar Variables de Entorno
Asegúrate de tener un archivo `.env` en la raíz de esta carpeta (`backend-avistar/`). El archivo `docker-compose.yml` requiere este archivo para configurar las variables de entorno de la aplicación.

### 2. Levantar el Backend y la Base de Datos
Dentro de esta misma carpeta (`backend-avistar/`), ejecuta el siguiente comando para levantar la API y la base de datos PostgreSQL:

```bash
docker compose up -d
```

Esto iniciará:
- **Base de Datos (PostgreSQL):** Disponible en el puerto `5428`.
- **Backend API (FastAPI):** Disponible en el puerto `8010` (mapeado internamente al 8000).

Puedes verificar que la API está corriendo accediendo a la documentación interactiva en tu navegador:
- **🔗 Swagger UI:** [http://localhost:8010/docs](http://localhost:8010/docs)

### 3. Levantar el Frontend
Una vez que el backend esté corriendo, dirígete a la carpeta del frontend para iniciarlo:

```bash
cd ../frontend-avistar
```

Tienes dos opciones para correr el frontend:
- **Opción A (Nativo):** Simplemente abre el archivo `index.html` en tu navegador web.
- **Opción B (Usando Docker/Nginx):** 
  ```bash
  docker build -t avistar-frontend .
  docker run -d -p 8080:80 avistar-frontend
  ```
  Y luego accede a [http://localhost:8080](http://localhost:8080) en tu navegador.

---

## 🗄️ Credenciales de Base de Datos (PostgreSQL)

Si necesitas conectarte a la base de datos desde un cliente SQL (como pgAdmin, DBeaver, etc.), puedes usar las siguientes credenciales expuestas localmente:

- **Host:** `localhost`
- **Puerto:** `5428`
- **Usuario:** `avistar_user`
- **Contraseña:** `avistar_password`
- **Base de Datos:** `avistar_db`

## 💻 Desarrollo Local (Sin Docker para Python)

Si deseas correr la API localmente sin Docker:
1. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Levanta la base de datos en Docker (`docker compose up db -d`).
3. Ejecuta el servidor de desarrollo:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```