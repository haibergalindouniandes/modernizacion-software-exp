from modelo import Automovil
import logging

# Configuración logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función que registra el automovil en la base de datos
def listar_automoviles_registrados(session):
    try:        
        return session.query(Automovil).order_by(Automovil.placa.asc()).all() 
    except Exception as e:
        logger.error(str(e))
        session.rollback()
        raise e
    finally:
        session.close()