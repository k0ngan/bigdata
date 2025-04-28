# DataHub – Actividad 1

**INFB6052 – Herramientas para Ciencia de Datos**

## Descripción del Proyecto
Este repositorio contiene un prototipo base llamado **DataHub**, desarrollado para la Actividad 1 del curso **INFB6052**. El objetivo principal es introducir el concepto de **Big Data** y configurar un sistema web funcional utilizando **Streamlit** y **MongoDB**.

## Estructura del Proyecto
```
datahub_repo/
├── home.py
├── pages/
│   └── contexto.py
├── db.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requisitos
- Python 3.10 o superior
- MongoDB (instalado y en ejecución localmente o acceso a un servidor remoto)
- Streamlit 1.34.0
- PyMongo 4.7.2

## Instalación

1. **Clonar el repositorio**
```bash
git clone <repo_url> datahub_repo
cd datahub_repo
```

2. **Crear y activar un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate    # En Windows: venv\Scripts\activate
```

3. **Instalar las dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar la URI de MongoDB**

Exportar la variable de entorno:
```bash
export MONGO_URI="mongodb://localhost:27017"    # En Windows: set MONGO_URI=mongodb://localhost:27017
```

## Ejecución del Sistema

Para correr la aplicación:
```bash
streamlit run home.py
```

Esto abrirá automáticamente el navegador con la interfaz de DataHub.

## Funcionalidades
- **Página de Inicio**: Introducción al sistema, imagen representativa y bibliografía.
- **Contexto Big Data**: Definición de Big Data, características principales, casos de uso reales.
- **CRUD de Ejemplo**:
  - Crear nuevos registros.
  - Leer registros existentes.
  - Actualizar valores de registros.
  - Eliminar registros.

## Observaciones
- Es importante mantener una estructura modular del proyecto.
- Se recomienda eliminar contenido no profesional encontrado en `pages/contexto.py` antes de la entrega final.
- El sistema está diseñado para ser extensible en futuras actividades.

## Licencia
MIT License

---
**Desarrollado para:** Universidad Técnica Metropolitana – Ingeniería Civil en Ciencia de Datos

**Profesor:** Dr. Ing. Michael Miranda Sandoval
