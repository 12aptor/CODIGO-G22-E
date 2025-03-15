import express, { type Express } from "express";
import { authRouter } from "./routes/auth.router";

const main = () => {
  const app: Express = express();
  const PORT = parseInt(process.env.PORT || "3000");

  app.get("/", (_, res) => {
    res.json({
      object: "application",
      error: "Unauthorized",
    });
  });

  app.use("/api/auth", authRouter);

  app.listen(PORT);
  console.log(`Server is running: http://localhost:${PORT}`);
};

main();
