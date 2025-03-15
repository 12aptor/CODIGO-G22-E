import express, { type Express } from "express";

const main = () => {
  const app: Express = express();
  const PORT = parseInt(process.env.PORT || "3000");

  app.get("/", (_, res) => {
    res.json({
      object: "application",
      error: "Unauthorized",
    });
  });

  app.listen(PORT);
  console.log(`Server is running: http://localhost:${PORT}`);
};

main();
