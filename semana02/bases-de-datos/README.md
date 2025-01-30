# PostgreSQL

## Crear tabla

```sql
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    director VARCHAR(100),
    year INT,
    length_minutes INT,
);
```

## Insertar registros

```sql
INSERT INTO movies (title, director, year, length_minutes)
VALUES ('Toy Story', 'John Lasseter', 1995, 81);
```