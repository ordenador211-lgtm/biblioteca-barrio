# Práctica Biblioteca de Barrio

## Diagrama de Componentes
```mermaid
graph TD
    main --> prestamos
    main --> catalogo
    main --> socios
    prestamos --> catalogo
    prestamos --> socios
  ## Diario del Proyecto
Se ha decidido rechazar la petición del cliente de acceder directamente a la lista de libros. Mantener el encapsulamiento y usar exclusivamente funciones públicas protege la arquitectura y evita un acoplamiento innecesario entre componentes.  