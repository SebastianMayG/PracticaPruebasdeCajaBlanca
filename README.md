# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# En Linux / macOS
source .venv/bin/activate
# En Windows
.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutando la clase main
python main.py

# Ejecutando para generar el reporte HTML
coverage run -m pytest .\procesar_credenciales_test.py
coverage report
