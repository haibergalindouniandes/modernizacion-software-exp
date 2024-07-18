# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log"

# Clase que contiene la estructura de un error cuando el api-key es invalido
class ApiKeyError(ApiError):
    code = 403
    description = "No tiene permisos para consumir este recurso"    