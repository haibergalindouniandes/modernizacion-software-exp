# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    message = "Error interno, por favor revise el log"

# Clase que contiene la estructura de error cuando el request es invalido
class RequestError(ApiError):
    code = 400
    message = "Los parametros de entrada son invalidos. Por favor consulte los logs"
    
# Clase que contiene la estructura de error cuando el api-key es invalido
class ApiKeyError(ApiError):
    code = 403
    message = "No tiene permisos para consumir este recurso"
    
# Clase que contiene la estructura de error cuando ya existe un automovil registrado
class AutomovilYaCreadoError(ApiError):
    code = 409
    message = "El automovil ya se encuentra creado en el sistema"    