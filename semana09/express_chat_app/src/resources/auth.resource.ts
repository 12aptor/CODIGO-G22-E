import type { Request, Response } from "express";
import { loginSchema, registerSchema } from "../schemas/auth.schema";
import { prisma } from "../config/prisma";
// import { getStorage, ref, uploadBytes } from "firebase/storage";
// import { firebaseApp } from "../config/firebase";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

export const register = async (req: Request, res: Response) => {
  try {
    const avatar = req.file;

    if (!avatar) {
      throw new Error("Avatar is required");
    }

    const { success, error, data } = await registerSchema.safeParseAsync(
      req.body
    );

    if (!success) {
      throw new Error(error.message);
    }
    console.log({ data });
    // Subir avatar a firebase
    // const storage = getStorage(firebaseApp);
    // const fileRef = ref(storage, `users/avatars/${avatar.originalname}`);
    // const uploadAvatar = await uploadBytes(fileRef, avatar.buffer);

    // if (!uploadAvatar.metadata) {
    //   throw new Error("Error uploading avatar");
    // }

    const user = await prisma.users.create({
      data: {
        username: data.username,
        email: data.email,
        password: await bcrypt.hash(data.password, 10),
        avatar: "sin avatar",
      },
      select: {
        id: true,
        username: true,
        email: true
      }
    });

    res.status(200).json({
      object: "create_user",
      data: user,
    });
  } catch (error) {
    if (error instanceof Error) {
      res.status(400).json({
        object: "create_user",
        error: error.message
      })
    }
  }
};

export const login = async (req: Request, res: Response) => {
  try {
    const {
      success,
      error,
      data
    } = await loginSchema.safeParseAsync(req.body);

    if (!success) {
      throw new Error(error.message);
    }

    const user = await prisma.users.findUnique({
      where: {
        email: data.email
      }
    })

    if (!user) {
      throw new Error("Invalid email or password");
    }

    const passwordCorrect = await bcrypt.compare(
      data.password,
      user.password
    )

    if (!passwordCorrect) {
      throw new Error("Invalid email or passsword");
    }

    const secretKey = process.env.SECRET_KEY!;

    const access = jwt.sign(
      {
        id: user.id,
        username: user.username,
        email: user.email
      },
      secretKey,
      {
        expiresIn: "7d"
      }
    )

    res.status(200).json({
      object: "login",
      message: "Logged in successfully",
      data: { access }
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
