export class Car {
  marca: string;
  placa: string;
  modelo: string;
  kilometraje: number;
  color: string;
  cilindraje: string;
  tipo_combustible: string;
  vendido: boolean;
  valor_venta: number;
  kilometraje_venta: number;
  id?: number;

  constructor(
    marca: string,
    placa: string,
    modelo: string,
    kilometraje: number,
    color: string,
    cilindraje: string,
    tipo_combustible: string,
    vendido: boolean,
    valor_venta: number,
    kilometraje_venta: number,
    id?: number
  ) {
    this.marca = marca;
    this.placa = placa;
    this.modelo = modelo;
    this.kilometraje = kilometraje;
    this.color = color;
    this.cilindraje = cilindraje;
    this.tipo_combustible = tipo_combustible;
    this.vendido = vendido;
    this.valor_venta = valor_venta;
    this.kilometraje_venta = kilometraje_venta;
    this.id = id;
  }
}
