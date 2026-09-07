from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n--- RESTAURANTE APP ---")
    print("1. Registrar producto")
    print("2. Registrar usuario")
    print("3. Registrar venta y control de stock")
    print("4. Buscar producto por código")
    print("5. Buscar usuario por identificación")
    print("6. Consultar ventas de un usuario")
    print("7. Listar todo")
    print("8. Salir")

def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                codigo = input("Código del producto: ")
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))
                
                prod = Producto(codigo, nombre, categoria, precio, stock)
                restaurante.registrar_producto(prod)
                print("¡Producto registrado exitosamente!")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '2':
            try:
                ide = input("Identificación (Cédula/ID): ")
                nombre = input("Nombre del usuario: ")
                correo = input("Correo electrónico: ")
                
                usu = Usuario(ide, nombre, correo)
                restaurante.registrar_usuario(usu)
                print("¡Usuario registrado exitosamente!")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '3':
            try:
                id_v = input("ID de la venta: ")
                ide_u = input("Identificación del usuario: ")
                cod_p = input("Código del producto: ")
                cant = int(input("Cantidad a vender: "))
                
                restaurante.registrar_venta(id_v, ide_u, cod_p, cant)
                print("¡Venta realizada y stock actualizado con éxito!")
            except ValueError as e:
                print(f"Error en la venta: {e}")

        elif opcion == '4':
            cod = input("Ingrese el código del producto a buscar: ")
            p = restaurante.buscar_producto_por_codigo(cod)
            if p:
                print(f"Encontrado -> Producto: {p.nombre} | Precio: ${p.precio} | Stock: {p.stock}")
            else:
                print("Producto no encontrado.")

        elif opcion == '5':
            ide = input("Ingrese la identificación del usuario a buscar: ")
            u = restaurante.buscar_usuario_por_id(ide)
            if u:
                print(f"Encontrado -> Usuario: {u.nombre} | Correo: {u.correo}")
            else:
                print("Usuario no encontrado.")

        elif opcion == '6':
            ide = input("Ingrese la identificación del usuario para ver sus ventas: ")
            ventas_usuario = restaurante.consultar_ventas_por_usuario(ide)
            if ventas_usuario:
                print(f"\n--- Ventas del usuario {ide} ---")
                for v in ventas_usuario:
                    print(f"Venta ID: {v.id_venta} | Producto: {v.codigo_producto} | Cantidad: {v.cantidad}")
            else:
                print("No se encontraron ventas para este usuario.")

        elif opcion == '7':
            print("\n--- PRODUCTOS REGISTRADOS ---")
            for p in restaurante.listar_productos():
                print(f"[{p.codigo}] {p.nombre} - ${p.precio} (Stock: {p.stock})")
            
            print("\n--- USUARIOS REGISTRADOS ---")
            for u in restaurante.listar_usuarios():
                print(f"[{u.identificacion}] {u.nombre}")

        elif opcion == '8':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()