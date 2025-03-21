# MongoDB

## Instalación

- Instalar MongoDB Server
- Instalar MongoDB Compass
- Instalar MongoDB Shell

## Abrir MongoDB Shell

```bash
mongosh
```

## Mostrar las bases de datos

```bash
show dbs
```

## Crear o conectar a una base de datos

```bash
use <nombre-base-de-datos>
```

## Crear una colección

```javascript
db.createCollection("nombre-coleccion")
ó
db.nombre_coleccion.insertOne({ key: "value" })
```

## Insertar datos en una colección

```javascript
db.customers.insertOne({ name: "John Doe", age: 30 })

db.customers.insertMany([
    { name: "Bob Smith", age: 35 },
    { name: "Alice Johnson", age: 33}
])

db.customers.insertOne({
    name: "Charlie Brown",
    age: 40,
    tags: ["cool", "funny"],
    address: {
        street: "123 Main St",
        city: "Anytown",
        state: "CA",
        coordinates: [-122.345, 47.678]
    }
})
```

## Consultar datos en una colección

```javascript
db.customers.find()
db.customers.find({
    name: "Alice Johnson"
})
db.customers.find({
    age: 30
})
db.customers.findOne({
    age: 30
})
```

## Actualizar datos en una colección

```javascript
db.customers.updateOne(
    { name: "Alice Johnson" },
    { $set: { age: 34 } }
)
db.customers.updateMany(
    { age: { $lt: 30 } },
    { $set: { age: 30 } }
)
```

## Eliminar datos en una colección

```javascript
db.customers.deleteOne({
    name: "Alice Johnson"
})
db.customers.deleteMany(
    { age: { $lt: 30 } }
)
```

## Eliminar propiedades de un documento

```javascript
db.customers.updateOne(
    { _id: ObjectId("67dcd17a50151d4e4db7123a") },
    { $unset: { tags: 1 } }
)
```

## Ordenar datos de una colección

```javascript
db.customers.find().sort({ age: 1 })
// 1: Ascendente
// -1: Descendente
```

## Limitar los resultados de una consulta

```javascript
db.customers.find().sort({ age: 1 }).limit(10)
```

## Paginacion

```javascript
db.customers.find().sort({ age: 1 }).limit(10).skip(20)
```

## Busquedas avanzadas

### Operadores de comparación
- $eq: Igual a
    ```javascript
    db.customers.find({
        age: { $eq: 30 }
    })
    ```

- $ne: No igual a
    ```javascript
    db.customers.find({
        age: { $ne: 30 }
    })
    ```

- $gt: Mayor que
    ```javascript
    db.customers.find({
        age: { $gt: 30 }
    })
    ```

- $gte: Mayor o igual que
    ```javascript
    db.customers.find({
        age: { $gte: 30 }
    })
    ```

- $lt: Menor que
    ```javascript
    db.customers.find({
        age: { $lt: 30 }
    })
    ```

- $lte: Menor o igual que
    ```javascript
    db.customers.find({
        age: { $lte: 30 }
    })
    ```

- $in: Incluye
    ```javascript
    db.customers.find({
        tags: { $in: ["cool"] }
    })
    ```

- $nin: No incluye
    ```javascript
    db.customers.find({
        tags: { $nin: ["cool"] }
    })
    ```

### Operadores lógicos

- $and: Todos los criterios deben cumplirse
    ```javascript
    db.customers.find({
        $and: [
            {
                age: { $gt: 30 }
            },
            {
                tags: { $in: ["cool"] }
            }
        ]
    })
    ```

- $or: Al menos un criterio debe cumplirse
    ```javascript
    db.customers.find({
        $or: [
            {
                age: { $gt: 30 }
            },
            {
                tags: { $in: ["cool"] }
            }
        ]
    })
    ```

- $not: Invierte la condición
    ```javascript
    db.customers.find({
        age: {
            $not: {
                $gt: 30
            }
        }
    })
    ```

- $nor: Invierte el operador $or
    ```javascript
    db.customers.find({
        $nor: [
            {
                age: { $gt: 30 }
            },
            {
                tags: { $in: ["cool"] }
            }
        ]
    })
    ```

### Operadores de elementos

- $exists: Verifica si existe un elemento
    ```javascript
    db.customers.find({
        tags: { $exists: true }
    })
    ```

- $type: Verifica el tipo de un elemento
    ```javascript
    db.customers.find({
        age: { $type: "number" }
    })
    ```

- $regex: Verifica si el valor coincide con una expresión regular
    ```javascript
    db.customers.find({
        name: { $regex: /^A/ }
    })
    ```

### Consultas en arrays

- $elemMatch: Verifica si un elemento es igual a un valor
    ```javascript
    db.customers.find({
        tags: {
            $elemMatch: {
                $eq: "cool"
            }
        }
    })
    ```

- $size: Verifica el tamaño de un array
    ```javascript
    db.customers.find({
        tags: {
            $size: 2
        }
    })
    ```