import express, { type Express } from "express";
import { userRouter } from "./routes/user.router";

const main = () => {
  const app: Express = express();
  const PORT = parseInt(process.env.PORT || "3000");

  app.use(express.json());
  app.get("/", (_, res) => {
    res.send("Hello World! 🤠");
  });

  app.use("/api/users", userRouter);

  app.listen(PORT);
  console.log(`Server is running on: http://localhost:${PORT}`);
};

main();
