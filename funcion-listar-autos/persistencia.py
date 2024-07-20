from modelo import Automovil
import logging

# Configuración logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función que registra el automovil en la base de datos
def listar_automoviles(session):
    try:        
        list_autos = session.query(Automovil).order_by(Automovil.placa.asc()).all() 
        return list_autos
    except Exception as e:
        logger.error(str(e))
        session.rollback()
        raise e
    finally:
        session.close()

