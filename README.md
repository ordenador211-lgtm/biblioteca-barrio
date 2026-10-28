# Práctica Biblioteca de Barrio

## Diagrama de Componentes
```mermaid
graph TD
    main --> prestamos
    main --> catalogo
    main --> socios
    prestamos --> catalogo
    prestamos --> socios