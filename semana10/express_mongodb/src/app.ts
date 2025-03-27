import express from "express";
import morgan from "morgan";
import { userRouter } from "./routes/user.router";

const main = async () => {
  const app = express();
  const PORT = 3000;

  app.use(express.json());
  app.use(morgan("dev"));

  app.use("/api/users", userRouter);

  app.listen(PORT);
  console.log(`Server is running: http://localhost:${PORT}`);
}

main();