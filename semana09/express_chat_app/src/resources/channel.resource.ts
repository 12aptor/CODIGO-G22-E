import type { Request, Response } from "express";
import { channelSchema } from "../schemas/channel.schema";
import { prisma } from "../config/prisma";

export const createChannel = async (req: Request, res: Response) => {
  try {
    const {
      success,
      error,
      data
    } = await channelSchema.safeParseAsync(
      req.body
    )

    if (!success) {
      throw new Error(error.message);
    }

    const channel = await prisma.channels.create({
      data: data
    })

    res.status(200).json({
      object: "create_channel",
      message: "Channel created successfully",
      data: channel
    })
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        object: "create_channel",
        error: error.message
      })
    }
  }
}

export const listChannels = async (_: Request, res: Response) => {
  try {
    const channels = await prisma.channels.findMany();

    res.status(200).json({
      object: "get_channels",
      data: channels
    })
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        object: "create_channel",
        error: error.message
      })
    }
  }
}