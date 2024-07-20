from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean

Base = declarative_base()

class Automovil(Base):
    __tablename__ = 'automovil'

    id = Column(Integer, primary_key=True)
    marca = Column(String)
    placa = Column(String)
    modelo = Column(String)
    kilometraje = Column(Float)
    color = Column(String)
    cilindraje = Column(String)
    tipo_combustible = Column(String)
    vendido = Column(Boolean)
    valor_venta = Column(Float)
    kilometraje_venta = Column(Float)

    def __init__(self, marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible, vendido, valor_venta, kilometraje_venta):
        self.marca = marca
        self.placa = placa
        self.modelo = modelo
        self.kilometraje = kilometraje
        self.color = color
        self.cilindraje = cilindraje
        self.tipo_combustible = tipo_combustible
        self.vendido = vendido
        self.valor_venta = valor_venta
        self.kilometraje_venta = kilometraje_venta

    def keys(self):
        return ('id', 'marca', 'placa', 'modelo', 'kilometraje', 'color', 'cilindraje', 'tipo_combustible', 'vendido', 'valor_venta', 'kilometraje_venta')

    def __getitem__(self, item):
        return getattr(self, item)
    
    # Función que retorna un diccionario a partir del modelo
    def to_dict(self):
        return {
            "id": str(self.id),
            "marca": self.marca,
            "placa": self.placa,
            "modelo": self.modelo,
            "kilometraje": self.kilometraje,
            "color": self.color,
            "cilindraje": self.cilindraje,
            "tipo_combustible": self.tipo_combustible,
            "vendido": self.vendido,
            "valor_venta": self.valor_venta,
            "kilometraje_venta": self.kilometraje_venta
        }