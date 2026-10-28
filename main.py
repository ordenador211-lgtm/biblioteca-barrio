# main.py
from catalogo import Catalogo, Libro
from socios import Socios
from prestamos import Prestamos

def iniciar_sistema():
    catalogo = Catalogo()
    socios = Socios()
    prestamos = Prestamos(catalogo, socios)

    # Datos de prueba iniciales
    catalogo.agregar_libro(Libro("L1", "El Quijote", "Miguel de Cervantes", 2))
    catalogo.agregar_libro(Libro("L2", "Cien años de soledad", "Gabriel García Márquez", 1))

    while True:
        print("\n--- BIBLIOTECA DE BARRIO ---")
        print("1. Buscar libro")
        print("2. Dar de alta socio")
        print("3. Realizar préstamo")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            termino = input("Introduce el título a buscar: ")
            resultados = catalogo.buscar(termino)
            if resultados:
                print("\nLibros encontrados:")
                for l in resultados:
                    disponibles = sum(1 for e in l.ejemplares.values() if e["estado"] == "disponible")
                    print(f"- ID: {l.id_libro} | {l.titulo} de {l.autor} (Disponibles: {disponibles}/{len(l.ejemplares)})")
            else:
                print("No se encontraron libros.")

        elif opcion == "2":
            id_s = input("Introduce ID del socio: ")
            nombre = input("Introduce nombre del socio: ")
            exito, msg = socios.dar_de_alta(id_s, nombre)
            print(msg)

        elif opcion == "3":
            id_s = input("Introduce ID del socio: ")
            id_l = input("Introduce ID del libro: ")
            exito, msg = prestamos.realizar_prestamo(id_s, id_l)
            print(msg)

        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main = iniciar_sistema
    # Ejecutar consola
    iniciar_sistema()