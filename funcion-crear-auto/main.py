from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo import Automovil, Base
from validadores import validar_api_key
from mapeadores import generar_respuesta_exitosa, generar_respuesta_error
import os

# Configura la conexión a la base de datos
DATABASE_URI = os.getenv('DATABASE_URI')
engine = create_engine(DATABASE_URI)
# Crear la tabla en la base de datos si no existe
Base.metadata.create_all(engine)
# Crear la sesion
Session = sessionmaker(bind=engine)

def crear_automovil(request):
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

    # Crea una nueva sesión
    session = Session()

    try:
        # Validar API-KEY
        validar_api_key(request)
        # Crea una nueva instancia de Automovil
        nuevo_automovil = Automovil(
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

        # Inserción en la tabla
        session.add(nuevo_automovil)
        session.commit()
        
        return generar_respuesta_exitosa(nuevo_automovil)
    except Exception as e:
        session.rollback()
        return generar_respuesta_error(e)
    finally:
        session.close()
