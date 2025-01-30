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

INSERT INTO movies (title, director, year, length_minutes)
VALUES
    ('Finding Nemo', 'Andrew Stanton', 2003, 100),
    ('The Incredibles', 'Brad Bird', 2004, 115),
    ('Ratatouille', 'Brad Bird', 2007, 111),
    ('Up', 'Pete Docter', 2009, 96),
    ('Toy Story 3', 'Lee Unkrich', 2010, 103),
    ('Inside Out', 'Pete Docter', 2015, 95),
    ('Coco', 'Lee Unkrich', 2017, 105),
    ('Toy Story 4', 'Josh Cooley', 2019, 100),
    ('Soul', 'Pete Docter', 2020, 100);
```