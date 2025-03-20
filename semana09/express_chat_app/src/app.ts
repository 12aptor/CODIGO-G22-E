import express, { type Express } from "express";
import { authRouter } from "./routes/auth.router";
import { Server } from "socket.io";
import { createServer } from "http"
import cors from "cors";
import morgan from "morgan";
import { channelRouter } from "./routes/channel.router";
import { prisma } from "./config/prisma";
import { messageRouter } from "./routes/message.router";

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
  app.use("/api/channels", channelRouter);
  app.use("/api/messages", messageRouter);

  io.on("connection", (socket) => {
    socket.on("join", (channel: string) => {
      socket.join(channel);
    })

    type Message = {
      content: string;
      channel: string;
      author_id: number;
    }

    socket.on("message", async (message: Message) => {
      const channel_id = parseInt(message.channel.split("-")[1])

      const newMessage = await prisma.messages.create({
        data: {
          content: message.content,
          author_id: message.author_id,
          channel_id: channel_id
        },
        include: {
          author: {
            select: {
              username: true
            }
          }
        }
      })

      io.to(message.channel).emit("message", newMessage);
    })
  })

  httpServer.listen(PORT);
  console.log(`Server is running: http://localhost:${PORT}`);
};

main();
