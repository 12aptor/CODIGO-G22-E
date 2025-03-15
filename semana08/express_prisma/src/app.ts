import express, { type Express } from "express";
import { userRouter } from "./routes/user.router";
import morgan from "morgan";
import fs from "fs";
import cors from "cors";
import { authMiddleware } from "./config/middleware";

const main = () => {
  const app: Express = express();
  const PORT = parseInt(process.env.PORT || "3000");

  const accessLogStream = fs.createWriteStream("api_requests.log", {
    flags: "a",
  });

  app.use(
    cors({
      origin: "http://example.com",
      credentials: true,
      methods: "GET,HEAD,PUT,PATCH,POST,DELETE",
    })
  );
  app.use(morgan("combined", { stream: accessLogStream }));
  app.use(morgan("dev"));
  app.use(express.json());
  app.get("/", (_, res) => {
    res.send("Hello World! 🤠");
  });

  app.use("/api/users", authMiddleware, userRouter);

  app.listen(PORT);
  console.log(`Server is running on: http://localhost:${PORT}`);
};

main();
