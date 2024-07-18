import logging

# Configuración logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función que realiza el mapeo de respuesta exitosa
def generar_respuesta_exitosa(response):
    logger.info(f'Automovil creado exitosamente: {response.id}')
    return {'code': 200, 'message': 'Automovil creado exitosamente', 'automovil_id': response.id}

# Función que realiza el mapeo de respuesta de error
def generar_respuesta_error(response):
    # Error controlado
    if response.code:
        logger.error(response.message)
        return {'code': response.code, 'message': response.message}, response.code
    # Error interno
    logger.error(str(response))
    return {'code': response.code, 'message': str(response)}, 500