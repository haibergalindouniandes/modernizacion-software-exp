from modelo import Automovil
import logging

# Configuración logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función que registra el automovil en la base de datos
def registrar_automovil(session, automovil):
    try:
        session.add(automovil)
        session.commit()
        return automovil.id
    except Exception as e:
        logger.error(str(e))
        session.rollback()
        raise e
    finally:
        session.close()

# Función que registra el automovil en la base de datos
def consultar_automovil_por_placa(session, placa):
    try:
        return session.query(Automovil).filter_by(placa=placa).first()
    except Exception as e:
        logger.error(str(e))
        session.close()
        raise e