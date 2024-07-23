from jsonschema import validate, ValidationError
from errores import ApiKeyError, RequestError, AutomovilYaCreadoError
import logging
import os

# Configuración logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Obtenemos las variables de entorno
API_KEY = os.getenv('API_KEY')

# Define el esquema JSON
automovil_schema = {
    "type": "object",
    "properties": {
        "marca": {"type": "string"},
        "placa": {"type": "string"},
        "modelo": {"type": "string"},
        "kilometraje": {"type": "number"},
        "color": {"type": "string"},
        "cilindraje": {"type": "string"},
        "tipo_combustible": {"type": "string"},
        "vendido": {"type": "boolean"},
        "valor_venta": {"type": "number"},
        "kilometraje_venta": {"type": "number"}
    },
    "required": ["marca", "placa", "modelo", "kilometraje", "color", "cilindraje", "tipo_combustible", "vendido", "valor_venta", "kilometraje_venta"]
}

# Función que permite validar el esquema recibido en el request
def validar_esquema(request, schema):
    try:
        validate(instance=request, schema=schema)
    except ValidationError as e:
        logger.error(str(e))
        raise RequestError

# Función que permite validar el esquema recibido para la creacion de un automovil
def validar_automovil_request(request):
    validar_esquema(request, automovil_schema)

# Función que permite validar si viene el header API-KEY y si es valido
def validar_api_key(headers):
    # Verificar el API-KEY en los headers
    api_key = headers.get('Api-Key')
    if not api_key or api_key != API_KEY:
        logger.error(str(ApiKeyError.message))
        raise ApiKeyError

# Función que permite validar si un auto ya se encuentra registrado
def validar_auto_existente(automovil):
    # Validar si ya hay un automovil registrado
    if automovil:
        logger.error(str(AutomovilYaCreadoError.message))
        raise AutomovilYaCreadoError