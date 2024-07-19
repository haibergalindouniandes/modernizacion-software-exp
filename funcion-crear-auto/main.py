from mapeadores import mapear_respuesta_exitosa, mapear_respuesta_error, mapear_entidad_a_dto
from validadores import validar_api_key, validar_auto_existente, validar_automovil_request
from persistencia import registrar_automovil, consultar_automovil_por_placa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from modelo import Base
import os

# Configura la conexión a la base de datos
DATABASE_URI = os.getenv('DATABASE_URI')
engine = create_engine(DATABASE_URI)
# Crear la tabla en la base de datos si no existe
Base.metadata.create_all(engine)
# Crear la sesion
Session = sessionmaker(bind=engine)

def crear_automovil(request):
    # Crea una nueva sesión
    session = Session()
    try:
        # Validar API-KEY
        validar_api_key(request)
        # Validar request
        validar_automovil_request(request)
        # Validar si ya se encuentra registrado el automovil
        validar_auto_existente(consultar_automovil_por_placa(session, request))
        # Inserción en la tabla
        automovil_id = registrar_automovil(session, mapear_entidad_a_dto(request))
        return mapear_respuesta_exitosa(automovil_id)
    except Exception as e:
        return mapear_respuesta_error(e)