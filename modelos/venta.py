class Venta:
    def __init__(self, id_venta: str, identificacion_usuario: str, codigo_producto: str, cantidad: int):
        self.id_venta = id_venta
        self.identificacion_usuario = identificacion_usuario
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad

    def a_diccionario(self) -> dict:
        return {
            "id_venta": self.id_venta,
            "identificacion_usuario": self.identificacion_usuario,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad
        }