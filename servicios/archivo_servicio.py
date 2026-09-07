import json
import os

class ArchivoServicio:
    DIR_DATOS = "datos"

    @staticmethod
    def _asegurar_directorio():
        os.makedirs(ArchivoServicio.DIR_DATOS, exist_ok=True)

    @staticmethod
    def guardar_datos(nombre_archivo: str, datos: list):
        ArchivoServicio._asegurar_directorio()
        ruta = os.path.join(ArchivoServicio.DIR_DATOS, nombre_archivo)
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print(f"Error: Sin permisos para escribir en {nombre_archivo}")

    @staticmethod
    def cargar_datos(nombre_archivo: str) -> list:
        ruta = os.path.join(ArchivoServicio.DIR_DATOS, nombre_archivo)
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Aviso: El archivo {nombre_archivo} está vacío o corrupto.")
            return []
        except PermissionError:
            print(f"Error: Sin permisos para leer {nombre_archivo}")
            return []