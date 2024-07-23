import logging
import json

# Configuración logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función que realiza el mapeo de respuesta exitosa
def generar_respuesta_exitosa(response, headers):
    response_json = json.dumps([auto.to_dict() for auto in response])
    logger.info(f'Automovil listados exitosamente: {response_json}')
    return (response_json, 200, headers)

# Función que realiza el mapeo de respuesta de error
def generar_respuesta_error(response, headers):
    # Error controlado
    if response.code:
        logger.error(response.message)
        return ({'code': response.code, 'message': response.message}, response.code, headers)
    # Error interno
    logger.error(str(response))
    return ({'code': response.code, 'message': str(response)}, 500, headers)

