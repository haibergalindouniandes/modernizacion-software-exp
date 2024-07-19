from modelo import Automovil
import logging

# Configuración logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función que registra el automovil en la base de datos
def registrar_automovil(session, request):
    try:
        session.add(request)
        session.commit()
        return request.id
    except Exception as e:
        logger.error(str(e))
        session.rollback()
        raise e
    finally:
        session.close()

# Función que registra el automovil en la base de datos
def consultar_automovil_por_placa(session, request):
    try:
        request_json = request.get_json()
        automovil = session.query(Automovil).filter_by(placa=request_json['placa']).first()
        return automovil
    except Exception as e:
        logger.error(str(e))
        session.close()
        raise e