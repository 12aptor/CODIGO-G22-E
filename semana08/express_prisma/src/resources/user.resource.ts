import type { Request, Response } from "express";
import { prisma } from "../config/prisma";

export const listUsers = async (_: Request, res: Response) => {
  try {
    const users = await prisma.user.findMany({
      orderBy: {
        id: "asc",
      },
    });
    res.status(200).json({
      object: "users_list",
      data: users,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        object: "users_list",
        error: error.message,
      });
    }
  }
};

export const createUser = async (req: Request, res: Response) => {
  try {
    const { name, email, password } = req.body;

    const user = await prisma.user.create({
      data: {
        name,
        email,
        password,
      },
    });

    res.status(200).json({
      object: "users_create",
      data: user,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        object: "users_list",
        error: error.message,
      });
    }
  }
};

export const updateUser = async (req: Request, res: Response) => {
  try {
    const { name, email, password } = req.body;
    const { userId } = req.params;

    const user = await prisma.user.findUnique({
      where: {
        id: parseInt(userId),
      },
    });

    if (!user) {
      throw new Error("User not found");
    }

    const updatedUser = await prisma.user.update({
      where: {
        id: parseInt(userId),
      },
      data: {
        name,
        email,
        password,
      },
    });

    res.status(200).json({
      object: "users_update",
      data: updatedUser,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        object: "users_list",
        error: error.message,
      });
    }
  }
};
