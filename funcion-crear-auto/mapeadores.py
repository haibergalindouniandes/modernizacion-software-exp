from modelo import Automovil
import logging

# Configuración logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Función que realiza el mapeo de respuesta exitosa
def mapear_respuesta_exitosa(automovil_id, headers):
    logger.info(f'Automovil creado exitosamente: {automovil_id}')
    return ({'code': 200, 'message': f'Automovil con ID [{automovil_id}] creado exitosamente'}, 200, headers)

# Función que realiza el mapeo de respuesta de error
def mapear_respuesta_error(response, headers):
    # Error controlado
    if response.code:
        logger.error(response.message)
        return ({'code': response.code, 'message': response.message}, response.code, headers)
    # Error interno
    logger.error(str(response))
    return ({'code': response.code, 'message': str(response)}, 500, headers)

# Función que realiza el mapeo de respuesta exitosa
def mapear_entidad_a_dto(request):
    # Obtén los datos del request
    request_json = request.get_json()
    marca = request_json['marca']
    placa = request_json['placa']
    modelo = request_json['modelo']
    kilometraje = request_json['kilometraje']
    color = request_json['color']
    cilindraje = request_json['cilindraje']
    tipo_combustible = request_json['tipo_combustible']
    vendido = request_json['vendido']
    valor_venta = request_json['valor_venta']
    kilometraje_venta = request_json['kilometraje_venta']
    
    return Automovil(
            marca=marca,
            placa=placa,
            modelo=modelo,
            kilometraje=kilometraje,
            color=color,
            cilindraje=cilindraje,
            tipo_combustible=tipo_combustible,
            vendido=vendido,
            valor_venta=valor_venta,
            kilometraje_venta=kilometraje_venta
        )