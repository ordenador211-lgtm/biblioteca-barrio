# prestamos.py
from datetime import datetime, timedelta

class Prestamos:
    def __init__(self, catalogo_componente, socios_componente):
        self.catalogo = catalogo_componente
        self.socios = socios_componente
        self.historial_prestamos = [] # Registro de préstamos activos

    def realizar_prestamo(self, id_socio, id_libro):
        # 1. Obtener socio mediante función pública
        socio = self.socios.obtener(id_socio)
        if not socio:
            return False, "Socio no encontrado."

        # 2. Comprobar regla extra: Socio sancionado
        if socio.esta_sancionado():
            return False, "El socio está sancionado y no puede pedir libros."

        # 3. Comprobar regla extra: Límite de 2 libros a la vez
        if len(socio.libros_prestados) >= 2:
            return False, "El socio ya tiene 2 libros prestados (límite máximo alcanzado)."

        # 4. Obtener libro mediante función pública
        libro = self.catalogo.obtener(id_libro)
        if not libro:
            return False, "Libro no encontrado."

        # 5. Intentar marcar como prestado en el catálogo
        exito, mensaje = self.catalogo.marcar_prestado(id_libro, id_socio)
        if exito:
            socio.libros_prestados.append(id_libro)
            fecha_prestamo = datetime.now()
            fecha_caducidad = fecha_prestamo + timedelta(days=7) # Caduca a los 7 días
            
            self.historial_prestamos.append({
                "id_socio": id_socio,
                "id_libro": id_libro,
                "fecha_prestamo": fecha_prestamo,
                "caducidad": fecha_caducidad
            })
            return True, f"Préstamo realizado con éxito. Fecha de devolución límite: {fecha_caducidad.strftime('%Y-%m-%d')}."
        
        return False, mensaje

    def registrar_devolucion(self, id_socio, id_libro):
        socio = self.socios.obtener(id_socio)
        if socio and id_libro in socio.libros_prestados:
            socio.libros_prestados.remove(id_libro)
            self.catalogo.marcar_devuelto(id_libro, id_socio)
            
            # Comprobar si caducó tarde para sancionar (opcional / simulado)
            return True, "Devolución registrada correctamente."
        return False, "No consta ese préstamo para el socio indicado."