import express from "express";

const main = async () => {
  const app = express();
  const PORT = 3000;

  app.get("/", (req, res) => {
    res.send("Bienvenido a mi aplicación! 😎")
  })

  app.listen(PORT);
  console.log(`Server is running: http://localhost:${PORT}`)
}

main();