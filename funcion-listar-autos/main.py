from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo import Automovil, Base
from validadores import validar_api_key
from mapeadores import  generar_respuesta_error
import os
import json

# Configura la conexión a la base de datos
DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
# Crear la tabla en la base de datos si no existe
Base.metadata.create_all(engine)
# Crear la sesion
Session = sessionmaker(bind=engine)

def listar_automovil(request):
    
    # Crea una nueva sesión
    session = Session()

    try:
        # Validar API-KEY
        validar_api_key(request)
        list_autos = session.query(Automovil).all() 
        json_response = []
        for auto in list_autos:
            json_response.append(auto.to_dict())

        return json.dumps(json_response),200,{'Content-Type': 'application/json'}
    except Exception as e:
        session.rollback()
        return generar_respuesta_error(e)
    finally:
        session.close()