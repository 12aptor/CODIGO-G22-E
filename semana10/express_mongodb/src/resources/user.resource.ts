import type { Request, Response } from "express";
import { prisma } from "../config/prisma";
import { userSchema } from "../schemas/user.schema";

export const getUsers = async (_: Request, res: Response) => {
  try {
    const users = await prisma.users.findMany();

    res.status(200).json({
      object: "users_list",
      data: users,
    })
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        object: "users_list",
        error: error.message,
      })
    }
  }
}

export const createUser = async (req: Request, res: Response) => {
  try {
    const { success, error, data } = await userSchema.safeParseAsync(req.body);

    if (!success) {
      throw new Error(error.message);
    }

    const user = await prisma.users.create({
      data: {
        name: data.name,
        email: data.email,
      }
    })

    res.status(200).json({
      object: "create_user",
      data: user,
    })
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        object: "create_user",
        error: error.message,
      })
    }
  }
}