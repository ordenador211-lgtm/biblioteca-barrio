# catalogo.py

class Libro:
    def __init__(self, id_libro, titulo, autor, total_ejemplares=1):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        # Cada título tiene varios ejemplares propios (disponibles, prestados, reservados)
        self.ejemplares = {
            i: {"estado": "disponible", "prestado_a": None} 
            for i in range(1, total_ejemplares + 1)
        }
        self.cola_reservas = [] # Lista de IDs de socios que han reservado

    def ejemplar_disponible(self):
        for eid, info in self.ejemplares.items():
            if info["estado"] == "disponible":
                return eid
        return None

class Catalogo:
    def __init__(self):
        self.libros = {} # id_libro -> Objeto Libro

    def agregar_libro(self, libro: Libro):
        self.libros[libro.id_libro] = libro

    def buscar(self, titulo_parcial):
        titulo_parcial = titulo_parcial.lower()
        return [l for l in self.libros.values() if titulo_parcial in l.titulo.lower()]

    def obtener(self, id_libro):
        return self.libros.get(id_libro)

    def marcar_prestado(self, id_libro, id_socio):
        libro = self.obtener(id_libro)
        if not libro:
            return False, "Libro no encontrado."
        
        eid = libro.ejemplar_disponible()
        if eid:
            libro.ejemplares[eid]["estado"] = "prestado"
            libro.ejemplares[eid]["prestado_a"] = id_socio
            return True, f"Ejemplar {eid} prestado con éxito."
        else:
            # Si no hay disponibles, se permite reservar
            if id_socio not in libro.cola_reservas:
                libro.cola_reservas.append(id_socio)
                return False, "No hay ejemplares disponibles. Libro añadido a tu lista de reservas."
            return False, "No hay ejemplares disponibles y ya tienes una reserva activa para este título."

    def marcar_devuelto(self, id_libro, id_socio):
        libro = self.obtener(id_libro)
        if not libro:
            return False
        for eid, info in libro.ejemplares.items():
            if info["estado"] == "prestado" and info["prestado_a"] == id_socio:
                info["estado"] = "disponible"
                info["prestado_a"] = None
                return True
        return False