from errors import ApiKeyError
import os

# Obtenemos las variables de entorno
API_KEY = os.getenv('API_KEY')

# Función que permite validar si viene el header API-KEY y si es valido
def validar_api_key(request):
    # Verificar el API-KEY en los headers
    api_key = request.headers.get('API-KEY')
    if not api_key or api_key != API_KEY:
        raise ApiKeyError