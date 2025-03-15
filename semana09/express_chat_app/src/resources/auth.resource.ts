import type { Request, Response } from "express";
import { registerSchema } from "../schemas/auth.schema";
import { prisma } from "../config/prisma";
import { getStorage, ref, uploadBytes } from "firebase/storage";

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

    // Subir avatar a firebase
    const storage = getStorage();
    const fileRef = ref(storage, `users/avatars/${avatar.originalname}`);
    const uploadAvatar = await uploadBytes(fileRef, avatar.buffer);

    if (!uploadAvatar.metadata) {
      throw new Error("Error uploading avatar");
    }

    const user = await prisma.users.create({
      data: {
        username: data.username,
        email: data.email,
        password: data.password,
        avatar: avatar.originalname,
      },
    });

    res.status(200).json({
      object: "create_user",
      data: user,
    });
  } catch (error) {}
};

// const login = () => {

// }
