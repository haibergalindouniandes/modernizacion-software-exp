from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo import Automovil, Base
from validadores import validar_api_key
from mapeadores import  generar_respuesta_error,generar_respuesta_exitosa
from persistencia import listar_automoviles_registrados
import functions_framework
import os

# Configura la conexión a la base de datos
DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
# Crear la tabla en la base de datos si no existe
Base.metadata.create_all(engine)
# Crear la sesion
Session = sessionmaker(bind=engine)

@functions_framework.http
def listar_automoviles(request):
    # Asignar headers
    headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,PATCH,OPTIONS",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Max-Age": "3600",
            "Content-Type": "application/json"
        }
    # Validar CORS
    if request.method == "OPTIONS":
        return ("", 200, headers)
    
    try:
        # Crea una nueva sesión
        session = Session()
        # Validar API-KEY
        validar_api_key(request.headers)
        return generar_respuesta_exitosa(listar_automoviles_registrados(session), headers)
    except Exception as e:
        return generar_respuesta_error(e, headers) 