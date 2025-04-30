# DataHub – Actividad 1

Prototipo base para el curso **INFB6052 – Herramientas para CS. de Datos**.

## Estructura

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

## Instalación

```bash
# 1. Clonar
git clone <repo_url> datahub_repo
cd datahub_repo

# 2. Entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
export MONGO_URI="mongodb://localhost:27017"
streamlit run home.py
```

## Licencia

MIT
