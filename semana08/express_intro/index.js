import express from 'express';

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware global
app.use((req, res, next) => {
    console.log('Middleware global');
    next();
})

// Ruta de inicio
app.get('/', (req, res) => {
    res.send('Hola mundo! 👋');
})

// Middleware para una ruta específica
app.get(
    '/home',
    (req, res, next) => {
        const url = req.url;
        const method = req.method;
        console.log(`Method: ${method}, URL: ${url}`);
        next();
    },
    (req, res) => {
        res.send('Hola en casa! 🏡');
    }
);

// Recuperar parametros de la URL
app.get("/users/:userName", (req, res) => {
    const userName = req.params.userName;
    res.send(`Hola ${userName}! 👋`);
})

app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
})