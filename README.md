Estudiante: Karla Daniela Luque Navarrete
Descripción del Sistema
Aplicación desarrollada en Python para la gestión de un restaurante, aplicando Programación Orientada a Objetos, persistencia local mediante archivos JSON y optimización del rendimiento en las búsquedas mediante el uso de diccionarios como índices en memoria.

Estructura del Proyecto
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
Responsabilidad de los Componentes
- modelos: Contiene las clases del dominio (Producto, Usuario y Venta) que representan las entidades del sistema y permiten serializar sus datos.
- servicios/archivo_servicio.py: Centraliza la lectura y escritura de los archivos JSON ubicados en la carpeta de datos.
- servicios/restaurante.py: Administra las colecciones principales (listas) y la lógica de negocio. Implementa diccionarios auxiliares en memoria para indexar productos y usuarios, optimizando las búsquedas frecuentes.
- main.py: Punto de entrada que coordina el menú interactivo por consola y gestiona la interacción con el usuario.

Mejoras de Rendimiento Aplicadas
- Índices con Diccionarios (dict)**: Se implementaron estructuras auxiliares en memoria (_indice_productos y _indice_usuarios) para buscar productos por código y usuarios por identificación de forma directa, evitando recorridos lineales innecesarios sobre las listas completas.
- Reconstrucción Automática: Al iniciar la aplicación y cargar los datos desde los archivos JSON, los índices se reconstruyen automáticamente para mantener la coherencia.
- Sincronización: Cada vez que se registran o modifican datos, los índices se actualizan simultáneamente junto con la persistencia en disco.

Instrucciones de Ejecución
1. Abra una terminal en la raíz del proyecto.
2. Ejecute el programa con el siguiente comando:
   ```bash
   python restaurante_app/main.py