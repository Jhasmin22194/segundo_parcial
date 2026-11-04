# Sistema de inventario y ventas

Monolito modular con Flask, SQLAlchemy y Bootstrap 

## Instalación
```bash
python -m venv venv
venv\Scripts\activate       
pip install -r requirements.txt
```

## Migraciones
```bash
flask --app run db init
flask --app run db migrate -m "migracion inicial"
flask --app run db upgrade
```

## Datos de prueba y ejecución
```bash
python seed.py
python run.py
```
Abrir http://127.0.0.1:5000
