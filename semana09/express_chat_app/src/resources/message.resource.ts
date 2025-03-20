import type { Request, Response } from "express"
import { prisma } from "../config/prisma";

export const listMessages = async (req: Request, res: Response) => {
  try {
    const channelId = parseInt(req.params.channelId);

    const messages = await prisma.messages.findMany({
      where: {
        channel_id: channelId
      },
      include: {
        author: {
          select: {
            username: true
          }
        }
      }
    })

    res.status(200).json({
      object: "get_messages",
      data: messages
    })
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        object: "create_user",
        error: error.message
      })
    }
  }
}