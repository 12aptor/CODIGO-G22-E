import express, { type Express } from "express";
import { authRouter } from "./routes/auth.router";
import { Server } from "socket.io";
import { createServer } from "http"
import cors from "cors";
import morgan from "morgan";

const main = () => {
  const app: Express = express();
  const PORT = parseInt(process.env.PORT || "3000");

  const httpServer = createServer(app);
  const io = new Server(httpServer, {
    cors: {
      origin: "*",
    }
  })

  app.use(express.json());
  app.use(cors());
  app.use(morgan("dev"));

  app.get("/", (_, res) => {
    res.json({
      object: "application",
      error: "Unauthorized",
    });
  });

  app.use("/api/auth", authRouter);

  io.on("connection", (socket) => {
    socket.on("join", (channel_id: string) => {
      socket.join(channel_id);
    })

    type Message = {
      content: string;
      channel_id: string;
      author_id: number;
    }

    socket.on("message", (message: Message) => {
      io.to(message.channel_id).emit("message", message);
    })
  })

  httpServer.listen(PORT);
  console.log(`Server is running: http://localhost:${PORT}`);
};

main();
