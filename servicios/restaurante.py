from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self):
        # Colecciones principales (listas)
        self.productos = []
        self.usuarios = []
        self.ventas = []
        
        # Estructuras auxiliares en memoria (diccionarios para índices de rendimiento)
        self._indice_productos = {}  # codigo -> Producto
        self._indice_usuarios = {}   # identificacion -> Usuario

        # Cargar datos y construir índices iniciales
        self.cargar_todo()

    def reconstruir_indices(self):
        """Reconstruye los diccionarios auxiliares a partir de las listas principales."""
        self._indice_productos = {p.codigo: p for p in self.productos}
        self._indice_usuarios = {u.identificacion: u for u in self.usuarios}

    def cargar_todo(self):
        """Carga datos desde JSON y reconstruye índices."""
        # Productos
        p_datos = ArchivoServicio.cargar_datos("productos.json")
        self.productos = [Producto(**d) for d in p_datos]

        # Usuarios
        u_datos = ArchivoServicio.cargar_datos("usuarios.json")
        self.usuarios = [Usuario(**d) for d in u_datos]

        # Ventas
        v_datos = ArchivoServicio.cargar_datos("ventas.json")
        self.ventas = [Venta(**d) for d in v_datos]

        self.reconstruir_indices()

    # --- PRODUCTOS ---
    def registrar_producto(self, producto: Producto):
        if producto.codigo in self._indice_productos:
            raise ValueError("Ya existe un producto con este código.")
        self.productos.append(producto)
        self._indice_productos[producto.codigo] = producto
        ArchivoServicio.guardar_datos("productos.json", [p.a_diccionario() for p in self.productos])

    def buscar_producto_por_codigo(self, codigo: str) -> Producto:
        """Búsqueda optimizada mediante diccionario índice O(1)."""
        return self._indice_productos.get(codigo)

    def listar_productos(self):
        return self.productos

    # --- USUARIOS ---
    def registrar_usuario(self, usuario: Usuario):
        if usuario.identificacion in self._indice_usuarios:
            raise ValueError("Ya existe un usuario con esta identificación.")
        self.usuarios.append(usuario)
        self._indice_usuarios[usuario.identificacion] = usuario
        ArchivoServicio.guardar_datos("usuarios.json", [u.a_diccionario() for u in self.usuarios])

    def buscar_usuario_por_id(self, identificacion: str) -> Usuario:
        """Búsqueda optimizada mediante diccionario índice O(1)."""
        return self._indice_usuarios.get(identificacion)

    def listar_usuarios(self):
        return self.usuarios

    # --- VENTAS Y STOCK ---
    def registrar_venta(self, id_venta: str, identificacion_usuario: str, codigo_producto: str, cantidad: int):
        # Validar existencia con índices
        usuario = self.buscar_usuario_por_id(identificacion_usuario)
        if not usuario:
            raise ValueError("El usuario no se encuentra registrado.")
        
        producto = self.buscar_producto_por_codigo(codigo_producto)
        if not producto:
            raise ValueError("El producto no existe.")
        
        if producto.stock < cantidad:
            raise ValueError("Stock insuficiente para realizar la venta.")

        # Descontar stock
        producto.stock -= cantidad

        # Registrar venta
        nueva_venta = Venta(id_venta, identificacion_usuario, codigo_producto, cantidad)
        self.ventas.append(nueva_venta)

        # Persistir cambios
        ArchivoServicio.guardar_datos("ventas.json", [v.a_diccionario() for v in self.ventas])
        ArchivoServicio.guardar_datos("productos.json", [p.a_diccionario() for p in self.productos])

    def consultar_ventas_por_usuario(self, identificacion: str) -> list:
        """Consulta ventas relacionadas con un usuario."""
        return [v for v in self.ventas if v.identificacion_usuario == identificacion]