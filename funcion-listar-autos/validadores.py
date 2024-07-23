from errores import ApiKeyError
import logging
import os

# Configuración logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Obtenemos las variables de entorno
API_KEY = os.getenv('API_KEY')

# Función que permite validar si viene el header API-KEY y si es valido
def validar_api_key(headers):
    # Verificar el API-KEY en los headers
    api_key = headers.get('Api-Key')
    if not api_key or api_key != API_KEY:
        logger.error(str(ApiKeyError.message))
        raise ApiKeyError